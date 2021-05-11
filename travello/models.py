from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    year = models.IntegerField()
    new = models.BooleanField(default=False)
