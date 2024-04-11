from django.urls import path
from kinopoisk.views import (
    movie_list, actor_list,
    director_list, genre_list,
    movie_detail, genre_detail,
    person_detail,
)

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('movie/<int:id>/', movie_detail, name='movie_detail'),
    path('actors/', actor_list, name='actor_list'),
    path('actor/<int:id>/', person_detail, name='person_detail'),
    path('directors/', director_list, name='director_list'),
    path('directors/<int:id>/', person_detail, name='person_detail'),
    path('genres/', genre_list, name='genre_list'),
    path('genre/<int:id>/', genre_detail, name='genre_detail'),
]
