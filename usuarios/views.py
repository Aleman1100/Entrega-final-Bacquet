from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from usuarios.forms import MiFormularioDeCreacion, EdicionPerfil
from usuarios.models import DatosExtra

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            
            django_login(request, user)
            
            DatosExtra.objects.get_or_create(user=request.user)
            
            return redirect('inicio')     
    
    return render(request,'usuarios/login.html', {'formulario_de_login': formulario})

def registro(request):
    formulario = MiFormularioDeCreacion()
    
    if request.method == 'POST':   
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('login')
        
    return render(request, 'usuarios/registro.html', {'formulario_de_registro': formulario})

def editar_perfil(request):
    
    datos_extra = request.user.datosextra
    
    formulario = EdicionPerfil(initial={'biografia': datos_extra.biografia, 'avatar': datos_extra.avatar}, instance=request.user)
    
    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            nueva_biografia = formulario.cleaned_data.get('biografia')
            nuevo_avatar = formulario.cleaned_data.get('avatar')
            
            if nueva_biografia:
                datos_extra.biografia = nueva_biografia
            if nuevo_avatar:
                datos_extra.avatar = nuevo_avatar
                
            datos_extra.save()                
            formulario.save()
            
            return redirect('detalle_perfil', datos_extra.id)           
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class CambiarPassword(PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html'
    success_url = reverse_lazy('logout')
    
class DetallePerfil(DetailView):
    model = DatosExtra
    template_name = 'usuarios/detalle_perfil.html'
    

