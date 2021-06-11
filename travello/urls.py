from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('action',views.action, name='action'),
    path('comedy',views.comedy, name='comedy'),
    path('romantic',views.romantic, name='romantic'),
    path('rom-com',views.romcom, name='rom-com'),
    path('adventure',views.adventure, name='adventure'),
    path('musical',views.musical, name='musical'),
    path('drama',views.drama, name='drama'),
    path('historical-drama',views.historicaldrama, name='historical-drama'),
    path('sci-fi',views.scifi, name='sci-fi'),
    path('movie/<str:slug>/<int:id>',views.movie,name='movie')
]

