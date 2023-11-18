from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from mangas.models import Manga
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListadoMangas(ListView):
    model = Manga
    context_object_name = 'listado_de_mangas'
    template_name = 'manga/mangas.html'
    
    def get_queryset(self):
        nombre_manga = self.request.GET.get('nombre_manga', '')
        if nombre_manga:
            listado_de_mangas = self.model.objects.filter(nombre_manga__icontains=nombre_manga)
        else:
            listado_de_mangas = self.model.objects.all()
        return listado_de_mangas
    
class CrearManga(LoginRequiredMixin,CreateView):
    model = Manga
    template_name = 'manga/crear_manga.html'
    fields = ['nombre_manga','tomos_manga','genero_manga']
    success_url = reverse_lazy('mangas')
    
class ActualizarManga(LoginRequiredMixin,UpdateView):
    model = Manga
    template_name = 'manga/actualizar_manga.html'
    fields = ['nombre_manga','tomos_manga','genero_manga']
    success_url = reverse_lazy('mangas')
    
class DetalleManga(DetailView):
    model = Manga
    template_name = 'manga/detalle_manga.html'
    
class EliminarManga(LoginRequiredMixin, DeleteView):
    model = Manga
    template_name = 'manga/eliminar_manga.html'
    success_url = reverse_lazy('mangas')
    
    