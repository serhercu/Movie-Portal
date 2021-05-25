from django.contrib import admin

from .models import Movie, Rate, Comment, Person, Director

# Register your models here.

admin.site.register(Movie)
admin.site.register(Rate)
admin.site.register(Comment)
admin.site.register(Person)
admin.site.register(Director)
