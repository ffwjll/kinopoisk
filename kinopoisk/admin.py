from django.contrib import admin

from kinopoisk.models import Genre, MoviePerson, Movie, MovieReview


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'birth_date', 'photo')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'rating',
        'release_date',
        'duration',
        'poster',
        'budget',
    )


@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'movie',
        'text',
        'likes',
        'created_at',
    )
