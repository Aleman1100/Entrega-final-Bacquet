from django.urls import path
from inicio.views import inicio, peliculas, crear_pelicula, eliminar_pelicula, actualizar_pelicula, detalle_pelicula, series, crear_serie, eliminar_serie, actualizar_serie, detalle_serie, libros, crear_libro, eliminar_libro, actualizar_libro, detalle_libro

urlpatterns = [
    path('', inicio, name='inicio'),
    path('peliculas/', peliculas, name='peliculas'),
    path('peliculas/crear/', crear_pelicula, name='crear_pelicula'),
    path('peliculas/<int:pelicula_id>/eliminar/', eliminar_pelicula, name='eliminar_pelicula'),
    path('peliculas/<int:pelicula_id>/actualizar/', actualizar_pelicula, name='actualizar_pelicula'),
    path('peliculas/<int:pelicula_id>/detalle/', detalle_pelicula, name='detalle_pelicula'),
    path('series/', series, name='series'),
    path('series/crear/', crear_serie, name='crear_serie'),
    path('series/<int:serie_id>/eliminar/', eliminar_serie, name='eliminar_serie'),
    path('series/<int:serie_id>/actualizar/', actualizar_serie, name='actualizar_serie'),
    path('series/<int:serie_id>/detalle/', detalle_serie, name='detalle_serie'),
    path('libros/', libros, name='libros'),
    path('libros/crear/', crear_libro, name='crear_libro'),
    path('libros/<int:libro_id>/eliminar/', eliminar_libro, name='eliminar_libro'),
    path('libros/<int:libro_id>/actualizar/', actualizar_libro, name='actualizar_libro'),
    path('libros/<int:libro_id>/detalle/', detalle_libro, name='detalle_libro'),
]
