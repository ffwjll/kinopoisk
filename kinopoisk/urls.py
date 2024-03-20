from django.urls import path
from kinopoisk.views import (
    movie_list, actor_list,
    director_list, genre_list,
)

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('actors/', actor_list, name='actor_list'),
    path('directors/', director_list, name='director_list'),
    path('genres/', genre_list, name='genre_list'),
]
