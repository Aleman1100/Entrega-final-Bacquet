from django.db import models

class Paleta(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.anio}'
    
class Pelicula(models.Model):
    nombre_pelicula = models.CharField(max_length=50)
    tipo_pelicula = models.TextField()
    duracion_pelicula = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre_pelicula} - {self.tipo_pelicula} - {self.duracion_pelicula}'
    
class Serie(models.Model):
    nombre_serie = models.CharField(max_length=50)
    tipo_serie = models.TextField()
    capitulos_serie = models.IntegerField()
    duracion_capitulos = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre_serie} - {self.tipo_serie} - {self.capitulos_serie} - {self.duracion_capitulos}'
    
class Libro(models.Model):
    nombre_libro = models.CharField(max_length=50)
    autor_libro = models.TextField()
    paginas_libro = models.IntegerField()
    editorial_libro = models.TextField()
    
    def __str__(self):
        return f'{self.nombre_libro} - {self.autor_libro} - {self.paginas_libro} - {self.editorial_libro}'