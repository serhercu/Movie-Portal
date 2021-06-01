import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Person(models.Model):
    Name = models.CharField(max_length=50)
    Role = models.BooleanField(default=True)

    def __str__(self):
        return self.Name


class Director(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class Comment(models.Model):
    Name = models.CharField(max_length=40)
    Comment = models.CharField(max_length=400)
    Date = models.DateTimeField('date published')

    def __str__(self):
        return self.Comment

class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True, default='')
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    year = models.IntegerField()
    new = models.BooleanField(default=False)
    Language = models.CharField(max_length=20, default='')
    CATEGORY_CHOICES = [
        ('AC', 'Action'),
        ('CO', 'Comedies'),
        ('RO', 'Romantic'),
        ('ROM', 'Rom-coms'),
        ('AD', 'Adventure'),
        ('MU', 'Musical'),
        ('DR', 'Drama'),
        ('HDR', 'Historical drama'),
        ('SC', 'Sci-fi'),
    ]
    Category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='CO')

    MeanRatings = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    NumberRates = models.IntegerField(default=0)
    numberLikes = models.IntegerField(default=0)
    numberDislikes = models.IntegerField(default=0)

    NumberComments = models.IntegerField(default=0)

    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    persons = models.ManyToManyField(Person)
    comments = models.ManyToManyField(Comment)
    link = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.title


class Rate(models.Model):
    Rate = models.BooleanField(default=True)
    Date = models.DateTimeField('date published')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.Rate

    def was_published_recently(self):
        return self.Date >= timezone.now() - datetime.timedelta(days=1)

