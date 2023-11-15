from django.urls import path
from mangas.views import ListadoMangas, CrearManga, ActualizarManga, DetalleManga, EliminarManga

urlpatterns = [
        path('mangas/', ListadoMangas.as_view(), name='mangas'),
        path('mangas/crear/', CrearManga.as_view(), name='crear_manga'),
        path('mangas/<int:pk>/', DetalleManga.as_view(), name='detalle_manga'),
        path('mangas/<int:pk>/actualizar/', ActualizarManga.as_view(), name='actualizar_manga'),
        path('mangas/<int:pk>/eliminar/', EliminarManga.as_view(), name='eliminar_manga'),        
    ]
    