from django.urls import path

from games.views import game_create, game_detail, game_list, game_join, get_player_list

app_name = "games"

urlpatterns = [
    path("create/", game_create, name="create"),
    path("detail/<int:id>/<slug:slug>/", game_detail, name="detail"),
    path('join/', game_join, name='join'),
    path('get_player_list/<int:game_id>/', get_player_list, name='get_player_list'),
    path('', game_list, name='list'),
]
