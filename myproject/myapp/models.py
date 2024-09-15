from django.db import models

class Favorite(models.Model):
    name = models.CharField(max_length=100)
    favorite_color = models.CharField(max_length=50)
    favorite_animal = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.favorite_color} - {self.favorite_animal}"
