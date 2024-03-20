from django.shortcuts import render


def movie_list(request):
    return render(request, 'kinopoisk/movies.html')


def actor_list(request):
    return render(request, 'kinopoisk/actors.html')

def director_list(request):
    return render(request, 'kinopoisk/directors.html')

def genre_list(request):
    return render(request, 'kinopoisk/genres.html')

