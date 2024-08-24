from django.urls import path

from location.views import football_fields

app_name = 'location'

urlpatterns = [
    path('locations/', football_fields, name='locations'),
]