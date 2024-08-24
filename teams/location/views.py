import requests
from django.shortcuts import render

from location.forms import CityForm


def football_fields(request):
    football_fields_data = None
    city = None
    coordinates = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["name"]
            coordinates = get_coordinates(city)
            football_fields_data = get_football_fields_data(city)
    else:
        city = request.GET.get("name", "Самара")
        coordinates = get_coordinates(city)
        football_fields_data = get_football_fields_data(city)

    form = CityForm()

    context = {
        "football_fields_data": football_fields_data,
        "form": form,
        "city": city,
        "coordinates": coordinates,
    }
    return render(request, "locations.html", context)


def get_football_fields_data(city):
    YOUR_KEY = "2c6f5ef9-bfc1-4fb3-9028-4d0362ee75da"
    BASE_URL = "https://catalog.api.2gis.com/3.0/items"

    url_city = f"{BASE_URL}?q={city}&key={YOUR_KEY}"
    response_city = requests.get(url_city)

    if response_city.status_code == 200:
        data_id = response_city.json()

    if 'result' in data_id and 'items' in data_id['result'] and data_id['result']['items']:
        city_id_full = data_id['result']['items'][0]['id']
        city_id = city_id_full.split('_')[0]

    url_location = f"{BASE_URL}?q=футбольное поле&city_id={city_id}&key={YOUR_KEY}"
    response_location = requests.get(url_location)
    football_fields_data = response_location.json()

    return football_fields_data

def get_coordinates(city):
    YOUR_KEY = "2c6f5ef9-bfc1-4fb3-9028-4d0362ee75da"
    BASE_URL = "https://catalog.api.2gis.com/3.0/items/geocode"

    url_geo = f"{BASE_URL}?q={city}&fields=items.point&key={YOUR_KEY}"
    response_geo = requests.get(url_geo)


    if response_geo.status_code == 200:
        data_id = response_geo.json()

    if 'result' in data_id and 'items' in data_id['result'] and data_id['result']['items']:
        point = data_id['result']['items'][0]['point']
        lat = point['lat']
        lon = point['lon']
        return [lon, lat]
    return None


