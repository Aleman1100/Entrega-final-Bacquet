from django.urls import path
from inicio.views import inicio, peliculas, crear_pelicula, series, crear_serie, libros, crear_libro

urlpatterns = [
    path('', inicio, name='inicio'),
    path('peliculas/', peliculas, name='peliculas'),
    path('peliculas/crear/', crear_pelicula, name='crear_pelicula'),
    path('series/', series, name='series'),
    path('series/crear/', crear_serie, name='crear_serie'),
    path('libros/', libros, name='libros'),
    path('libros/crear/', crear_libro, name='crear_libro')
]
