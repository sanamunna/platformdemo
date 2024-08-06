from django.urls import path
from . import views
# app_name='mvapp'
urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movies/category/<slug:category_slug>/', views.movie_list_by_category, name='movie_list_by_category'),
    path('movies/<slug:movie_slug>/', views.movie_detail, name='movie_detail'),
    path('add-movie/', views.add_movie, name='add_movie'),
    path('movies/<slug:movie_slug>/review/',views.post_review,name='post_review'),
    path('modify/<slug:movie_slug>/',views.modify,name='modify'),
    path('delete/<slug:movie_slug>/',views.delete,name='delete'),
]