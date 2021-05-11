from django.contrib import admin

from .models import Movie
from .models import Rate
from .models import Comment
from .models import Person

# Register your models here.

admin.site.register(Movie)
admin.site.register(Rate)
admin.site.register(Comment)
admin.site.register(Person)