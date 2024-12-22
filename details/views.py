from django.shortcuts import render, get_object_or_404, redirect
from renderer.models import Poster, Favorite

# Create your views here.
def poster_details(request, id):
    poster = get_object_or_404(Poster, pk=id)
    is_favorite = Favorite.objects.filter(poster=poster).exists()
    return render(request, 'poster_details.html', {'poster': poster, 'is_favorite': is_favorite})

def add_to_favorites(request, poster_id):
    if request.method == 'POST':
        poster = get_object_or_404(Poster, id=poster_id)
        if not Favorite.objects.filter(poster=poster).exists():
            Favorite.objects.create(poster=poster)

    return redirect('favorite')

def remove_from_favorites(request, poster_id):
    poster = get_object_or_404(Poster, id=poster_id)
    favorite = Favorite.objects.filter(poster=poster).first()

    if favorite:
        favorite.delete()

    return redirect('favorite')
