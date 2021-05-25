from django.shortcuts import render
from .models import Movie, Comment

# Create your views here.


def index(request):
    dests = Movie.objects.all().order_by('-id')

    return render(request, 'index.html', {'dests': dests})

def search(request):
    title1 = request.GET['title1']
    year1 = request.GET['year']

    movies = Movie.objects.all()
    searched = []

    for movie in movies:
        if title1 in movie.title:
            searched.append(movie) 
        elif year1 == movie.year:
            if int(year1) == movie.year:
                searched.append(movie)
    
    return render(request,'search.html', {'searched': searched})

def movie(request, slug, id):
    movie = Movie.objects.get(id=id)

    return render(request,'movie.html', {'movie': movie})
