from django.shortcuts import render, redirect
# Importar modelos
from inicio.models import Pelicula,Serie,Libro
# Importar los formularios de creacion.
from inicio.forms import CrearPeliculaFormulario,CrearSerieFormulario,CrearLibroFormulario
# Importar los formularios de busqueda.
from inicio.forms import BusquedaPeliculaFormulario,BusquedaSerieFormulario,BusquedaLibroFormulario

def inicio(request):
    
    return render(request, 'inicio/inicio.html', {})

def crear_pelicula(request):

    if request.method == 'POST':
        formulario = CrearPeliculaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            nombre_pelicula = info_limpia.get('nombre_pelicula')
            tipo_pelicula = info_limpia.get('tipo_pelicula')
            duracion_pelicula = info_limpia.get('duracion_pelicula')
            
            pelicula = Pelicula(nombre_pelicula=nombre_pelicula, tipo_pelicula=tipo_pelicula, duracion_pelicula=duracion_pelicula)
            pelicula.save()   
            
            return redirect('peliculas')
        else:
            return render(request,'inicio/crear_pelicula.html',{'formulario':formulario})
    
    formulario = CrearPeliculaFormulario()
    return render(request,'inicio/crear_pelicula.html',{'formulario':formulario})

def crear_serie(request):

    if request.method == 'POST':
        formulario = CrearSerieFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            nombre_serie = info_limpia.get('nombre_serie')
            tipo_serie = info_limpia.get('tipo_serie')
            capitulos_serie = info_limpia.get('capitulos_serie')
            duracion_capitulos = info_limpia.get('duracion_capitulos')
            
            serie = Serie(nombre_serie=nombre_serie, tipo_serie=tipo_serie, capitulos_serie=capitulos_serie, duracion_capitulos=duracion_capitulos)
            serie.save()   
            
            return redirect('series')
        else:
            return render(request,'inicio/crear_serie.html',{'formulario':formulario})
    
    formulario = CrearSerieFormulario()
    return render(request,'inicio/crear_serie.html',{'formulario':formulario})

def crear_libro(request):

    if request.method == 'POST':
        formulario = CrearLibroFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            nombre_libro = info_limpia.get('nombre_libro')
            autor_libro = info_limpia.get('autor_libro')
            paginas_libro = info_limpia.get('paginas_libro')
            editorial_libro = info_limpia.get('editorial_libro')
            
            libro = Libro(nombre_libro=nombre_libro, autor_libro=autor_libro, paginas_libro=paginas_libro, editorial_libro=editorial_libro)
            libro.save()   
            
            return redirect('libros')
        else:
            return render(request,'inicio/crear_libro.html',{'formulario':formulario})
    
    formulario = CrearLibroFormulario()
    return render(request,'inicio/crear_libro.html',{'formulario':formulario})

def peliculas(request):
        
    formulario = BusquedaPeliculaFormulario(request.GET)
    if formulario.is_valid():
        pelicula_a_buscar = formulario.cleaned_data.get('nombre_pelicula')
        listado_de_peliculas = Pelicula.objects.filter(nombre_pelicula__icontains=pelicula_a_buscar)
      
    return render(request, 'inicio/peliculas.html',{'listado_de_peliculas':listado_de_peliculas})

def series(request):
        
    formulario = BusquedaSerieFormulario(request.GET)
    if formulario.is_valid():
        serie_a_buscar = formulario.cleaned_data.get('nombre_serie')
        listado_de_series = Serie.objects.filter(nombre_serie__icontains=serie_a_buscar)
      
    return render(request, 'inicio/series.html',{'listado_de_series':listado_de_series})

def libros(request):
        
    formulario = BusquedaLibroFormulario(request.GET)
    if formulario.is_valid():
        libro_a_buscar = formulario.cleaned_data.get('nombre_libro')
        listado_de_libros = Libro.objects.filter(nombre_libro__icontains=libro_a_buscar)
      
    return render(request, 'inicio/libros.html',{'listado_de_libros':listado_de_libros})