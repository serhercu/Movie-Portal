from django.db import models

# Create your models here.

class Director(models.Model):
    class Meta:
        verbose_name_plural = 'director'

    name = models.CharField(max_length=75)

    def __str__(self):
        return super().__str__()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    year = models.IntegerField()
    new = models.BooleanField(default=False)

from django.db import models

# Create your models here.

class Director(models.Model):
    class Meta:
        verbose_name_plural = 'directors'

    name = models.CharField(max_length=75)

    def __str__(self):
        return super().__str__()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    year = models.IntegerField()

    class Genre(models.TextChoices):
            ACTION ='Action'
            CARTOON = 'Cartoon'
            HUMOR = 'Humor'
            THRILLER = 'Thriller'

    genre = models.TextField(choices=Genre.choices, default=0)

    director = models.ForeignKey(Director, on_delete=models.CASCADE, unique=True)

