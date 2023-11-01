from django import forms

# Formularios para creacion de datos

class CrearPeliculaFormulario(forms.Form):
    nombre_pelicula = forms.CharField(max_length=50)
    tipo_pelicula = forms.CharField(max_length=30)
    duracion_pelicula = forms.IntegerField()
    
class CrearSerieFormulario(forms.Form):
    nombre_serie = forms.CharField(max_length=50)
    tipo_serie = forms.CharField(max_length=30)
    capitulos_serie = forms.IntegerField()
    duracion_capitulos = forms.IntegerField()
    
class CrearLibroFormulario(forms.Form):
    nombre_libro = forms.CharField(max_length=50)
    autor_libro = forms.CharField(max_length=30)
    paginas_libro = forms.IntegerField()
    editorial_libro = forms.CharField(max_length=30)

# Busquedas de elementos en BBDD
   
class BusquedaPeliculaFormulario(forms.Form):
    nombre_pelicula = forms.CharField(max_length=50, required=False)
    
class BusquedaSerieFormulario(forms.Form):
    nombre_serie = forms.CharField(max_length=50, required=False)
    
class BusquedaLibroFormulario(forms.Form):
    nombre_libro = forms.CharField(max_length=50, required=False)
