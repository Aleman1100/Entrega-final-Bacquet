from django.urls import path
from animes.views import ListadoAnimes, CrearAnime, ActualizarAnime, DetalleAnime, EliminarAnime

urlpatterns = [
        path('animes/', ListadoAnimes.as_view(), name='animes'),
        path('animes/crear/', CrearAnime.as_view(), name='crear_anime'),
        path('animes/<int:pk>/', DetalleAnime.as_view(), name='detalle_anime'),
        path('animes/<int:pk>/actualizar/', ActualizarAnime.as_view(), name='actualizar_anime'),
        path('animes/<int:pk>/eliminar/', EliminarAnime.as_view(), name='eliminar_anime'),         
    ]