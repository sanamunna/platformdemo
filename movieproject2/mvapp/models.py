from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='movie_posters')
    description = models.TextField()
    release_date = models.DateField()
    actors = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_link = models.URLField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    class Meta:
        ordering=('name',)
        verbose_name='movie'
        verbose_name_plural='movies'


    def __str__(self):
        return self.name


class Review(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    rating=models.IntegerField(default=0)
    review=models.TextField()
