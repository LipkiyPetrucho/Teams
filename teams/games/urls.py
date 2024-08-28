from django.urls import path

from games.views import game_create, validate_address, game_detail

app_name = "games"

urlpatterns = [
    path("create/", game_create, name="create"),
    path("validate-address/", validate_address, name="validate_address"),
    path('detail/<int:id>/<slug:slug>/', game_detail, name='detail'),
]
