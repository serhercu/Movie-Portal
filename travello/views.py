from django.shortcuts import render
from .models import Movie, Comment
from datetime import date

# Create your views here.


def index(request):
    dests = Movie.objects.all().order_by('-id')

    return render(request, 'index.html', {'dests': dests})

def search(request):
    title = request.GET['title']
    year = request.GET['year']
    director = request.GET['director']
    genre = request.GET['genre']

    searched = []

    if not title and not year and not director and not genre:
        return render(request,'search.html', {'searched':searched})

    movies = Movie.objects.all()

    for movie in movies:
        if title != "":
            if title.lower() in movie.title.lower():
                searched.append(movie) 
        elif year != "":
            if int(year) == movie.year:
                searched.append(movie)
        elif director != "":
            if director in movie.director.Name:
                searched.append(movie)
        elif genre != "":
            if genre == movie.Category:
                searched.append(movie)
    
    return render(request,'search.html', {'searched': searched})

def action(request):
    movies1 = Movie.objects.all()
    dests = []
    
    for movie in movies1:
        if movie.Category == "AC":
            dests.append(movie)

    return render(request, 'index.html', {'dests': dests})

def comedy(request):
    movies1 = Movie.objects.all()
    dests = []
    
    for movie in movies1:
        if movie.Category == "CO":
            dests.append(movie)

    return render(request, 'index.html', {'dests': dests})

def romantic(request):
    movies1 = Movie.objects.all()
    dests = []
    
    for movie in movies1:
        if movie.Category == "RO":
            dests.append(movie)

    return render(request, 'index.html', {'dests': dests})

def romcom(request):
    movies1 = Movie.objects.all()
    dests = []
    
    for movie in movies1:
        if movie.Category == "ROM":
            dests.append(movie)

    return render(request, 'index.html', {'dests': dests})

def adventure(request):
    movies1 = Movie.objects.all()
    dests = []
    
    for movie in movies1:
        if movie.Category == "AD":
            dests.append(movie)

    return render(request, 'index.html', {'dests': dests})

def musical(request):
    movies1 = Movie.objects.all()
    dests = []
    
    for movie in movies1:
        if movie.Category == "MU":
            dests.append(movie)

    return render(request, 'index.html', {'dests': dests})

def drama(request):
    movies1 = Movie.objects.all()
    dests = []
    
    for movie in movies1:
        if movie.Category == "DR":
            dests.append(movie)

    return render(request, 'index.html', {'dests': dests})

def historicaldrama(request):
    movies1 = Movie.objects.all()
    dests = []
    
    for movie in movies1:
        if movie.Category == "HDR":
            dests.append(movie)

    return render(request, 'index.html', {'dests': dests})

def scifi(request):
    movies1 = Movie.objects.all()
    dests = []
    
    for movie in movies1:
        if movie.Category == "SC":
            dests.append(movie)

    return render(request, 'index.html', {'dests': dests})

def movie(request, slug, id):
    movie = Movie.objects.get(id=id)

    if request.method == 'POST':
        user = request.POST.get('user')
        text = request.POST.get('comment')

        comment = Comment(Name=user, Comment=text, Date=date.today())
        comment.save()
        movie.comments.add(comment)
        movie.save()
        

    return render(request,'movie.html', {'movie': movie})
