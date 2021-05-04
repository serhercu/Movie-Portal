from django.shortcuts import render
from .models import Movie

# Create your views here.


def index(request):
    dests = Movie.objects.all()

    return render(request, 'index.html', {'dests': dests})
