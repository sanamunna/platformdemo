from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from mvapp.models import Category,Movie,Review
from . forms import MovieForm


# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    categories = Category.objects.all()
    return render(request, 'movie_list.html', {'movies': movies, 'categories': categories})

def movie_detail(request, movie_slug):
    movie = Movie.objects.get(slug=movie_slug)
    reviews = Review.objects.filter(movie=movie)
    if request.method == 'POST':
        rating=request.POST['rating']
        review_text = request.POST['review']
        review = Review(movie=movie, rating=rating, review=review_text)
        review.save()
        return redirect('movie_detail', movie_slug)
    return render(request,'movie_detail.html',{'movie':movie,'reviews':reviews})


@login_required
def add_movie(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        description = request.POST['description']
        release_date = request.POST['release_date']
        actors = request.POST['actors']
        category_slug = request.POST['category']
        category = Category.objects.get(slug=category_slug)
        trailer_link = request.POST['trailer_link']
        movie = Movie(
            name=name,
            slug=slugify(name),
            image=image,
            description=description,
            release_date=release_date,
            actors=actors,
            category=category,
            trailer_link=trailer_link,
        )
        movie.save()
        return redirect('movie_list')
    else:
        categories=Category.objects.all()
        return render(request,'add_movie.html',{'categories':categories}    )

def movie_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    movies = Movie.objects.filter(category=category)
    return render(request, 'movie_list.html', {'movies': movies, 'category': category})

def post_review(request,movie_slug):
    movie=Movie.objects.get(slug=movie_slug)
    if request.method == 'POST':
        rating=request.POST['rating']
        review_text=request.POST['review']
        review=Review(movie=movie,rating=rating,review=review_text)
        review.save()
        return redirect('movie_detail',movie_slug)
    return render(request,'post_review.html')

@login_required
def modify(request,movie_slug):
    movie=Movie.objects.get(slug=movie_slug)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
@login_required
def delete(request,movie_slug):
    if request.method == 'POST':
        movie=Movie.objects.get(slug=movie_slug)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')