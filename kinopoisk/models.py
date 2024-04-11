from django.db import models

from core.models import User


class Genre(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()


class MoviePerson(models.Model):
    class RoleTypes(models.TextChoices):
        ACTOR = 'actor', 'Actor'
        DIRECTOR = 'director', 'Director'

    role = models.CharField(
        choices=RoleTypes.choices,
        max_length=15
    )
    name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(
        upload_to='kinopoisk/images/person/photos/',
        null=True, blank=True
    )


class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.PositiveSmallIntegerField()
    poster = models.ImageField(
        upload_to='kinopoisk/images/movies/posters/',
        null=True, blank=True
    )
    genres = models.ManyToManyField(to=Genre, related_name='movies')
    actors = models.ManyToManyField(to=MoviePerson, related_name='acted_in_movies')
    directors = models.ManyToManyField(to=MoviePerson, related_name='directed_movies')
    budget = models.PositiveIntegerField()


# actor = MoviePerson.objects.get(id=1, name='')
# movies = actor.acted_in_movies.all()

class MovieReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
