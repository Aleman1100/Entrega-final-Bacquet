from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from mangas.models import Manga
from django.urls import reverse_lazy

class ListadoMangas(ListView):
    model = Manga
    context_object_name = 'listado_de_mangas'
    template_name = 'manga/mangas.html'
    
class CrearManga(CreateView):
    model = Manga
    template_name = 'manga/crear_manga.html'
    fields = ['nombre_manga','tomos_manga','genero_manga']
    success_url = reverse_lazy('mangas')
    
class ActualizarManga(UpdateView):
    model = Manga
    template_name = 'manga/actualizar_manga.html'
    fields = ['nombre_manga','tomos_manga','genero_manga']
    success_url = reverse_lazy('mangas')
    
class DetalleManga(DetailView):
    model = Manga
    template_name = 'manga/detalle_manga.html'
    
class EliminarManga(DeleteView):
    model = Manga
    template_name = 'manga/eliminar_manga.html'
    success_url = reverse_lazy('mangas')
    