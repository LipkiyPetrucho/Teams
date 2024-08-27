from django.urls import path

from games.views import game_create

app_name = "games"

urlpatterns = [
    path("create/", game_create, name="create"),
]
