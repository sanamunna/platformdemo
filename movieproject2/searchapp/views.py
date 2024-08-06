from django.shortcuts import render, redirect
from mvapp.models import Movie
from django.db.models import Q
# Create your views here.

def SearchResult(request):
    movies=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movies=Movie.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request,'search.html',{'query':query,'movies':movies})
    else:
        return redirect('mvapp:movie_list')

