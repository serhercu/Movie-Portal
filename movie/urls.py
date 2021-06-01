from django.urls import path

from . import views

urlpatterns = [
    path('<str:slug>/<int:id>/like',views.like, name='like'),
    path('<str:slug>/<int:id>/dislike',views.dislike, name='dislike')
]