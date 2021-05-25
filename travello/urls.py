from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('search/',views.search, name='search'),
    path('movie/<str:slug>/<int:id>',views.movie,name='movie')
]

