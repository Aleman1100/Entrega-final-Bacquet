from django.db import models

class Anime(models.Model):

    nombre_anime = models.CharField(max_length=50)
    capitulos_anime = models.IntegerField()
    inicio_anime = models.DateField()
    
    def __str__(self):
        return f'{self.nombre_anime} - {self.capitulos_anime} - {self.inicio_anime}'
