from django.shortcuts import render, get_object_or_404
from renderer.models import Poster

# Create your views here.
def poster_details(request, id):
    poster = get_object_or_404(Poster, pk=id)
    return render(request, 'details/poster_details.html', {'poster': poster})
