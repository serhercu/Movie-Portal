import datetime
from django.contrib.postgres.fields import ArrayField

from django.db import models
from django.utils import timezone


# Create your models here.

class Person(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Director(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class Comment(models.Model):
    Name = models.CharField(max_length=40)
    Comment = models.CharField(max_length=2000)
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
    numberLikes = models.IntegerField(default=0)
    numberDislikes = models.IntegerField(default=0)

    NumberComments = models.IntegerField(default=0)

    Voters = ArrayField(models.CharField(max_length=10), blank=True, default=list)

    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    persons = models.ManyToManyField(Person, blank=True)
    comments = models.ManyToManyField(Comment, blank=True)
    link = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.title

