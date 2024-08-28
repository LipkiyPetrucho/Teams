from django.urls import path

from games.views import game_create, game_detail

app_name = "games"

urlpatterns = [
    path("create/", game_create, name="create"),
    path("detail/<int:id>/<slug:slug>/", game_detail, name="detail"),
]
