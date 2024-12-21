from django.db import models

# Create your models here.
class Poster(models.Model):
    url = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.url
