from django.contrib import admin
from .models import Poster, Favorite

# Register your models here.
class PosterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director_name', 'description', 'url')

admin.site.register(Poster)
admin.site.register(Favorite)
