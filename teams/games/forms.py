from django import forms
from django.forms import Select, TextInput, NumberInput, Textarea

from .models import Game


class GameCreateForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            "sport",
            "city",
            "place",
            "date",
            "start_time",
            "duration",
            "max_players",
            "price",
            "description",
        ]
        labels = {
            "sport": "Вид спорта",
            "city": "Город",
            "place": "Место игры",
            "date": "Дата игры",
            "start_time": "Время начала игры",
            "duration": "Продолжительность",
            "max_players": "Количество игроков",
            "price": "Цена игры",
            "description": "Описание",
        }

        widgets = {
            "sport": Select(
                attrs={
                    "class": "form-control form-control-width",
                    "style": "background-color: #f8f9fa; border-radius: 5px;",
                }
            ),
            "city": TextInput(
                attrs={
                    "class": "form-control form-control-width",
                    "style": "background-color: #f8f9fa; border-radius: 5px;",
                    "placeholder": "Введите название города",
                    "name": "location",
                    "id": "id_location",
                    "autocomplete": "off",
                }
            ),
            "place": TextInput(
                attrs={
                    "class": "form-control form-control-width",
                    "style": "background-color: #f8f9fa; border-radius: 5px;",
                    "placeholder": "Введите место игры",
                }
            ),
            "max_players": NumberInput(
                attrs={
                    "class": "form-control form-control-width",
                    "step": "1",
                    "style": "background-color: #f8f9fa; border-radius: 5px;",
                }
            ),
            "description": Textarea(
                attrs={
                    "cols": 30,
                    "rows": 3,
                    "class": "form-control form-control-width",
                    "type": "text",
                    "placeholder": "Опишите например: есть душевые, есть парковочные места",
                    "aria-label": "default input example",
                    "style": "background-color: #f8f9fa; border-radius: 5px;",
                }
            ),
            "price": NumberInput(
                attrs={
                    "step": "10",
                    "class": "form-control form-control-width",
                    "style": "background-color: #f8f9fa; border-radius: 5px;",
                    "placeholder": "Введите цену игры",
                }
            ),
            "duration": TextInput(
                attrs={
                    "placeholder": "HH:MM",
                    "type": "time",
                    "class": "form-control form-control-width",
                    "style": "background-color: #f8f9fa; border-radius: 5px;",
                }
            ),
            "date": TextInput(
                attrs={
                    "placeholder": "HH:MM",
                    "type": "date",
                    "class": "form-control form-control-width",
                    "style": "background-color: #f8f9fa; border-radius: 5px;",
                }
            ),
            "start_time": TextInput(
                attrs={
                    "placeholder": "HH:MM",
                    "type": "time",
                    "class": "form-control form-control-width",
                    "style": "background-color: #f8f9fa; border-radius: 5px;",
                }
            ),
        }
