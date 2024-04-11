from django.shortcuts import render

from kinopoisk.models import Movie, MoviePerson, Genre


def movie_list(request):
    return render(request, 'kinopoisk/movies.html', {
        'movies': Movie.objects.all()
    })


def movie_detail(request, id):
    return render(request, 'kinopoisk/movie_detail.html',{
        'movie': Movie.objects.get(id=id)
    })

def director_list(request):
    persons = MoviePerson.objects.filter(role=MoviePerson.RoleTypes.DIRECTOR)
    return render(request, 'kinopoisk/person_list.html', {
        'persons': persons
    })

def actor_list(request):
    persons = MoviePerson.objects.filter(role=MoviePerson.RoleTypes.ACTOR)
    return render(request, 'kinopoisk/person_list.html', {
        'persons': persons
    })

def person_detail(request, id):
    return render(request, 'kinopoisk/person_detail.html', {
        'person': MoviePerson.objects.get(id=id)
    })


def genre_list(request):
    return render(request, 'kinopoisk/genres.html', {
        'genres': Genre.objects.all()
    })


def genre_detail(request, id):
    return render(request, 'kinopoisk/genre_detail.html', {
        'genre': Genre.objects.get(id=id)
    })
