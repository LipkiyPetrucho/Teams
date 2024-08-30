from django.urls import path

from games.views import game_create, game_detail, game_list, game_join

app_name = "games"

urlpatterns = [
    path("create/", game_create, name="create"),
    path("detail/<int:id>/<slug:slug>/", game_detail, name="detail"),
    path('join/', game_join, name='join'),
    path('', game_list, name='list'),
]
