from django.shortcuts import render
from travello.models import Movie, Comment
from datetime import date

# Create your views here.

def like(request, slug, id):
    movie = Movie.objects.get(id=id)
    movie.numberLikes += 1

    movie.MeanRatings = round(movie.numberLikes / (movie.numberLikes + movie.numberDislikes) * 100, 2)

    movie.save()
    return render(request,'movie.html', {'movie': movie})


def dislike(request, slug, id):
    movie = Movie.objects.get(id=id)
    movie.numberDislikes += 1

    movie.MeanRatings = round(movie.numberLikes / (movie.numberLikes + movie.numberDislikes) * 100, 2)

    movie.save()
    return render(request,'movie.html', {'movie': movie})