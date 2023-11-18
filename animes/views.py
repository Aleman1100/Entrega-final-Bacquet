from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from animes.models import Anime
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListadoAnimes(ListView):
    model = Anime
    context_object_name = 'listado_de_animes'
    template_name = 'anime/animes.html'
        
    def get_queryset(self):
        nombre_anime = self.request.GET.get('nombre_anime', '')
        if nombre_anime:
            listado_de_animes = self.model.objects.filter(nombre_anime__icontains=nombre_anime)
        else:
            listado_de_animes = self.model.objects.all()
        return listado_de_animes
    
class CrearAnime(LoginRequiredMixin, CreateView):
    model = Anime
    template_name = 'anime/crear_anime.html'
    fields = ['nombre_anime','capitulos_anime','inicio_anime']
    success_url = reverse_lazy('animes')
    
class ActualizarAnime(LoginRequiredMixin, UpdateView):
    model = Anime
    template_name = 'anime/actualizar_anime.html'
    fields = ['nombre_anime','capitulos_anime','inicio_anime']
    success_url = reverse_lazy('animes')
    
class DetalleAnime(DetailView):
    model = Anime
    template_name = 'anime/detalle_anime.html'
    
class EliminarAnime(LoginRequiredMixin, DeleteView):
    model = Anime
    template_name = 'anime/eliminar_anime.html'
    success_url = reverse_lazy('mangas')
