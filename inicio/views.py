from django.shortcuts import render, redirect
# Importar modelos
from inicio.models import Pelicula,Serie,Libro
# Importar los formularios de creacion.
from inicio.forms import CrearPeliculaFormulario,CrearSerieFormulario,CrearLibroFormulario
# Importar los formularios de busqueda.
from inicio.forms import BusquedaPeliculaFormulario,BusquedaSerieFormulario,BusquedaLibroFormulario
# Importar los formularios de actualizacion.
from inicio.forms import ActualizarPeliculaFormulario,ActualizarSerieFormulario,ActualizarLibroFormulario
from django.contrib.auth.decorators import login_required

def inicio(request):
    
    return render(request, 'inicio/inicio.html', {})

##
#CRUD#
##

#
#Crear - Create
#

@login_required
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

@login_required
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

@login_required
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

#
#Listado - Read
#

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

#
#Eliminar - Delete
#

@login_required
def eliminar_pelicula(request, pelicula_id):
    pelicula_a_eliminar = Pelicula.objects.get(id=pelicula_id)
    pelicula_a_eliminar.delete()
    
    return redirect("peliculas")

@login_required    
def eliminar_serie(request, serie_id):
    serie_a_eliminar = Serie.objects.get(id=serie_id)
    serie_a_eliminar.delete()
    
    return redirect("series")

@login_required    
def eliminar_libro(request, libro_id):
    libro_a_eliminar = Libro.objects.get(id=libro_id)
    libro_a_eliminar.delete()
    
    return redirect("libros")

#
#Actualizar - Update
#

@login_required
def actualizar_pelicula(request, pelicula_id):
    pelicula_a_actualizar = Pelicula.objects.get(id=pelicula_id)
    
    if request.method == "POST":
        formulario = ActualizarPeliculaFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            pelicula_a_actualizar.nombre_pelicula = info_nueva.get('nombre_pelicula')
            pelicula_a_actualizar.tipo_pelicula = info_nueva.get('tipo_pelicula')
            pelicula_a_actualizar.duracion_pelicula = info_nueva.get('duracion_pelicula')
            
            pelicula_a_actualizar.save()
            return redirect('peliculas')
        else:
            return render(request, 'inicio/actualizar_pelicula.html', {'formulario':formulario})
    
    formulario = ActualizarPeliculaFormulario(initial={'nombre_pelicula': pelicula_a_actualizar.nombre_pelicula, 'tipo_pelicula': pelicula_a_actualizar.tipo_pelicula, 'duracion_pelicula': pelicula_a_actualizar.duracion_pelicula})    
    return render(request, 'inicio/actualizar_pelicula.html', {'formulario':formulario})

@login_required    
def actualizar_serie(request, serie_id):
    serie_a_actualizar = Serie.objects.get(id=serie_id)
    
    if request.method == "POST":
        formulario = ActualizarSerieFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            serie_a_actualizar.nombre_serie = info_nueva.get('nombre_serie')
            serie_a_actualizar.tipo_serie = info_nueva.get('tipo_serie')
            serie_a_actualizar.capitulos_serie = info_nueva.get('capitulos_serie')
            serie_a_actualizar.duracion_capitulos = info_nueva.get('duracion_capitulos')
            
            serie_a_actualizar.save()
            return redirect('series')
        else:
            return render(request, 'inicio/actualizar_serie.html', {'formulario':formulario})
    
    formulario = ActualizarSerieFormulario(initial={'nombre_serie': serie_a_actualizar.nombre_serie, 'tipo_serie': serie_a_actualizar.tipo_serie, 'capitulos_serie': serie_a_actualizar.capitulos_serie, 'duracion_capitulos': serie_a_actualizar.duracion_capitulos})    
    return render(request, 'inicio/actualizar_serie.html', {'formulario':formulario})

@login_required
def actualizar_libro(request, libro_id):
    libro_a_actualizar = Libro.objects.get(id=libro_id)
    
    if request.method == "POST":
        formulario = ActualizarLibroFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            libro_a_actualizar.nombre_libro = info_nueva.get('nombre_libro')
            libro_a_actualizar.autor_libro = info_nueva.get('autor_libro')
            libro_a_actualizar.paginas_libro = info_nueva.get('paginas_libro')
            libro_a_actualizar.editorial_libro = info_nueva.get('editorial_libro')
            
            libro_a_actualizar.save()
            return redirect('libros')
        else:
            return render(request, 'inicio/actualizar_libro.html', {'formulario':formulario})
    
    formulario = ActualizarLibroFormulario(initial={'nombre_libro': libro_a_actualizar.nombre_libro, 'autor_libro': libro_a_actualizar.autor_libro, 'paginas_libro': libro_a_actualizar.paginas_libro, 'editorial_libro': libro_a_actualizar.editorial_libro})    
    return render(request, 'inicio/actualizar_libro.html', {'formulario':formulario})

#
#Detalle
#

def detalle_pelicula(request,pelicula_id):
    pelicula = Pelicula.objects.get(id=pelicula_id)   
    return render(request, 'inicio/detalle_pelicula.html', {'pelicula': pelicula})

def detalle_serie(request,serie_id):
    serie = Serie.objects.get(id=serie_id)   
    return render(request, 'inicio/detalle_serie.html', {'serie': serie})

def detalle_libro(request,libro_id):
    libro = Libro.objects.get(id=libro_id)   
    return render(request, 'inicio/detalle_libro.html', {'libro': libro})