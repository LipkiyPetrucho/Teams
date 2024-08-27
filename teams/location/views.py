import os

import requests
from django.conf import settings
from django.shortcuts import render

from location.forms import CityForm


def football_fields(request):
    football_fields_data = None
    city = None
    coordinates = None
    if request.method == "POST":
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
    url_city = f"{settings.BASE_URL}?q={city}&key={os.getenv.YOUR_KEY}"
    print(f"URL для города: {url_city}")

    response_city = requests.get(url_city)

    if response_city.status_code == 200:
        data_id = response_city.json()

        if (
            "result" in data_id
            and "items" in data_id["result"]
            and data_id["result"]["items"]
        ):
            city_id_full = data_id["result"]["items"][0]["id"]
            city_id = city_id_full.split("_")[0]

            url_location = f"{settings.BASE_URL}?q=футбольное поле&city_id={city_id}&key={os.getenv.YOUR_KEY}"
            print(f"URL для футбольного поля: {url_location}")
            response_location = requests.get(url_location)
            football_fields_data = response_location.json()

            return football_fields_data


def get_coordinates(city):
    url_geo = f"{settings.BASE_URL_GEOCODE}?q={city}&fields=items.point&key={os.getenv.YOUR_KEY}"
    response_geo = requests.get(url_geo)

    if response_geo.status_code == 200:
        data_id = response_geo.json()

        if (
            "result" in data_id
            and "items" in data_id["result"]
            and data_id["result"]["items"]
        ):
            point = data_id["result"]["items"][0]["point"]
            lat = point["lat"]
            lon = point["lon"]
            return [lon, lat]
    return None
