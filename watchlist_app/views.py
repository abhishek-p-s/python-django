from django.shortcuts import render
from watchlist_app import models
from django.http import JsonResponse

def movie_list(request):
    movies = models.Movie.objects.all()
    data={
        'movies':list(movies.values())
    }
    return JsonResponse(data) # will only work with dictionaries
    
    
def movie_details(request, id):
    movie = models.Movie.objects.get(id=id)
    data={
        'name':movie.name,
        'description':movie.description,
        'active':movie.active
    }
    return JsonResponse(data)    
