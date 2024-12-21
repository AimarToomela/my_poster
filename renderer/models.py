from django.db import models

# Create your models here.
class Poster(models.Model):
    url = models.CharField(max_length=256, unique=True)
    name = models.CharField(max_length=256, default = "No name available")
    description = models.TextField(default = "No description available")
    director_name = models.CharField(max_length=256, default = "No director name available")

    def __str__(self):
        return self.url
