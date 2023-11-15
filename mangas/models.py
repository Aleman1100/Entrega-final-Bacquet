from django.db import models

class Manga(models.Model):

    nombre_manga = models.CharField(max_length=50)
    tomos_manga = models.IntegerField()
    genero_manga = models.CharField(max_length=15)
    
    def __str__(self):
        return f'{self.nombre_manga} - {self.tomos_manga} - {self.genero_manga}'