from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("players/", views.player_list, name="player_list"),
    path("players/<int:id>/", views.player_detail, name="player_detail"),
    path("players/add/", views.add_player, name="add_player"),
    path(
        "players/edit/<int:id>/",
        views.edit_player,
        name="edit_player"
    ),
    path(
    "players/delete/<int:id>/",
    views.delete_player,
    name="delete_player"
    ),
    
    path(
    "about/",
    views.about,
    name="about"
    ),
    
    path(
    "compare/",
    views.compare_players,
    name="compare_players",
    ),
    
    path(
    "favorite/<int:player_id>/",
    views.add_favorite,
    name="add_favorite",
    ),
    
    path(
    "favorites/",
    views.favorite_players,
    name="favorite_players",
    ),
    
    path(
    "favorites/remove/<int:player_id>/",
    views.remove_favorite,
    name="remove_favorite",
    ),
    
    path(
    "contact/",
    views.contact,
    name="contact",
    ),
]