from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages

from django.utils import timezone

from .models import Movie, Comment
from datetime import date


# Create your views here.


def index(request):
    movies = Movie.objects.all().order_by('-id')

    paginator = Paginator(movies, 9)
    page = request.GET.get('page')
    movies = paginator.get_page(page)

    search = False

    context = {
        'movies': movies,
        'search': search
    }

    if request.method == 'GET':
        title = request.GET.get('title')
        year = request.GET.get('year')
        director = request.GET.get('director')
        genre = request.GET.get('genre')

        movies = []
        search = True

        if not title and not year and not director and not genre:
            search = True
            return render(request, 'index.html', context)

        movies1 = Movie.objects.all()

        for movie in movies1:
            if title != "":
                if title.lower() in movie.title.lower():
                    movies.append(movie)
            elif year != "":
                if int(year) == movie.year:
                    movies.append(movie)
            elif director != "":
                if director.lower() in movie.director.Name.lower():
                    movies.append(movie)
            elif genre != "":
                if genre == movie.Category:
                    movies.append(movie)

        context = {
            'movies': movies,
            'search': search
        }

    return render(request, 'index.html', context)


def movie(request, slug, id):
    movie = Movie.objects.get(id=id)
    movies = Movie.objects.filter(Category=movie.Category)

    if request.method == 'POST':
        if request.user.is_authenticated:
            if 'send' in request.POST:
                user = request.POST.get('user')
                text = request.POST.get('comment')

                comment = Comment(Name=user, Comment=text, Date=timezone.now())
                comment.save()
                movie.comments.add(comment)
                movie.NumberComments += 1
                movie.save()
            else:
                found = False
                for x in movie.Voters:
                    if x == str(request.user.id): found = True

                if not found:
                    if 'like' in request.POST:
                        movie.numberLikes += 1
                    elif 'dislike' in request.POST:
                        movie.numberDislikes += 1
                        movie.Voters.append(str(request.user.id))
                        movie.save()
                else:
                    messages.info(request, 'You already voted this film!', extra_tags='vote')
        else:
            if 'send' in request.POST:
                messages.info(request, 'You should log in to comment!', extra_tags='comment')
            else:
                messages.info(request, 'You should log in to vote!', extra_tags='vote')

    if movie.numberLikes + movie.numberDislikes != 0:
        movie.MeanRatings = round(movie.numberLikes / (movie.numberLikes + movie.numberDislikes) * 100, 2)

    context = {
        'movie': movie,
        'movies': movies
    }

    return render(request, 'movie.html', context)


def action(request):
    movies1 = Movie.objects.all()
    movies = []

    for movie in movies1:
        if movie.Category == "AC":
            movies.append(movie)

    return render(request, 'index.html', {'movies': movies})


def comedy(request):
    movies1 = Movie.objects.all()
    movies = []

    for movie in movies1:
        if movie.Category == "CO":
            movies.append(movie)

    return render(request, 'index.html', {'movies': movies})


def romantic(request):
    movies1 = Movie.objects.all()
    movies = []

    for movie in movies1:
        if movie.Category == "RO":
            movies.append(movie)

    return render(request, 'index.html', {'movies': movies})


def romcom(request):
    movies1 = Movie.objects.all()
    movies = []

    for movie in movies1:
        if movie.Category == "ROM":
            movies.append(movie)

    return render(request, 'index.html', {'movies': movies})


def adventure(request):
    movies1 = Movie.objects.all()
    movies = []

    for movie in movies1:
        if movie.Category == "AD":
            movies.append(movie)

    return render(request, 'index.html', {'movies': movies})


def musical(request):
    movies1 = Movie.objects.all()
    movies = []

    for movie in movies1:
        if movie.Category == "MU":
            movies.append(movie)

    return render(request, 'index.html', {'movies': movies})


def drama(request):
    movies1 = Movie.objects.all()
    movies = []

    for movie in movies1:
        if movie.Category == "DR":
            movies.append(movie)

    return render(request, 'index.html', {'movies': movies})


def historicaldrama(request):
    movies1 = Movie.objects.all()
    movies = []

    for movie in movies1:
        if movie.Category == "HDR":
            movies.append(movie)

    return render(request, 'index.html', {'movies': movies})


def scifi(request):
    movies1 = Movie.objects.all()
    movies = []

    for movie in movies1:
        if movie.Category == "SC":
            movies.append(movie)

    return render(request, 'index.html', {'movies': movies})
