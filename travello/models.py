import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model):
    Name = models.CharField(max_length=50)
    Role = models.BooleanField(default=True)

    def __str__(self):
         return self.Name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    year = models.IntegerField()
    new = models.BooleanField(default=False)
'''    Title = models.CharField(max_length=200, unique=True, default='')
    Language = models.CharField(max_length=20, default='')
    CATEGORY_CHOICES = [
	('AC','Action'),
	('CO','Comedies'),
	('RO','Romantic'),
	('ROM','Rom-coms'),
	('AD','Adventure'),
	('MU','Musical'),
	('DR','Drama'),
	('HDR','Historical drama'),
	('SC','Sci-fi'),
    ]
    Category = models.CharField(max_length=3,choices=CATEGORY_CHOICES, default='CO')
    ReleaseDate = models.DateTimeField('date published', default=timezone.now)
    Description = models.CharField(max_length=1000, default='')
    MeanRatings = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    NumberRates = models.IntegerField(default=0)
    NumberComments = models.IntegerField(default=0)
    
    persons = models.ManyToManyField(Person)

    def __str__(self):
         return self.Title
'''

class Rate(models.Model): 
    Rate = models.BooleanField(default=True)
    Date = models.DateTimeField('date published')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
         return self.Rate  

    def was_published_recently(self):
         return self.Date >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model): 
    Comment = models.CharField(max_length=400)
    Date = models.DateTimeField('date published')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
         return self.Comment  
