from django.shortcuts import render
from .models import Poster

# Create your views here.
def favorite(request):
    poster = Poster.objects.last()
    return render(request, 'favorite.html', {'poster': poster})

def top(request, size):
    try:
        size = int(size)
        posters = Poster.objects.all().order_by('-id')[:size]
        return render(request, 'top.html', {'posters': posters})

    except ValueError:
        return render(request, 'top.html', {'error': 'Invalid size parameter. Please provide a '
                                                     'valid number.'})
