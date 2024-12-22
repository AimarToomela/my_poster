from django.shortcuts import render
from .models import Poster, Favorite

# Create your views here.
def favorite(request):
    poster = Poster.objects.last()
    return render(request, 'favorite.html', {'poster': poster})

def top(request, size=None):
    if size:
        try:
            size = int(size)
            posters = Poster.objects.all().order_by('-id')[:size]
        except ValueError:
            posters = Poster.objects.all().order_by('-id')[:5]
    else:
        posters = Poster.objects.all().order_by('-id')[:5]
    return render(request, 'top.html', {'posters': posters})

def favorites(request):
    favorite_posters = Poster.objects.filter(id__in=Favorite.objects.values('poster_id'))
    if not favorite_posters.exists():
        error = "No favorite posters found"
    else:
        error = None
    return render(request, 'favorite.html', {'posters': favorite_posters})
