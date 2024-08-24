from django.forms import ModelForm, TextInput

from location.models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ["name"]
        widgets = {
            "city": TextInput(
                attrs={
                    "class": "form-control mr-2",
                    "placeholder": "Enter city name",
                    "name": "city",
                    "id": "id_city",
                    "autocomplete": "off",
                }
            )
        }