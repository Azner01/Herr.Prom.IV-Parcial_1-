from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

#Vista de la página principal
def pagina_principal(request):
    return render(request, 'menu_principal.html')

#Vistas asociada al modelo de evento

class lista_eventos(ListView):
    model = evento
    template_name = 'lista_eventos.html'


def crear_eventos(request):
    if request.method == 'POST':
        form = formularioEvento(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = formularioEvento()
    return render(request, 'crear_evento.html', {'form': form})


class editar_evento(UpdateView):
    model = evento
    form_class = formularioEvento
    template_name = 'editar_eventos.html'
    success_url ="."

    def get_object(self):
        id = self.kwargs.get('pk')
        return evento.objects.get(id = id)
    
    def get_success_url(self):
        return reverse('eventosApp:lista_Eventos')
    

class eliminar_evento(DeleteView):
    model = evento
    template_name = 'eliminar_evento.html'
    success_url ="/gestor_eventos/eventos/"



#Vistas asociada al modelo de organizador


class organizador_lista(ListView):
    model = organizador
    template_name = 'lista_organizadores.html'


class organizador_añadir(CreateView):
    model = organizador
    fields = ['nombre_org']
    template_name = 'añadir_organizadores.html'
    success_url = '/gestor_eventos/organizadores/'



class organizador_editar(UpdateView):
    model = organizador
    fields = ['nombre_org']
    template_name = 'editar_organizador.html'
    success_url ="."

    def get_object(self):
        id = self.kwargs.get('pk')
        return organizador.objects.get(id = id)
    
    def get_success_url(self):
        return reverse('eventosApp:lista_organizadores')

class organizador_eliminar(DeleteView):
    model = organizador
    template_name = 'eliminar_organizador.html'
    success_url ="/gestor_eventos/organizadores/"

#Vistas asociada al modelo de inicio de sesión

def pagina_registro(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Cuenta fue creada por ' + user)
            return redirect('.')
    else:
        form = CreateUserForm()
    #Diseño de la página obtenido: https://jsfiddle.net/ivanov11/hzf0jxLg/
    return render(request, 'registro_login.html', {'form': form})

def pagina_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('../home')
        else:
            messages.info(request, 'Usuario o contraseña incorrectas')
            return render(request, 'login.html', context)
    
    #Diseño de la página obtenido: https://jsfiddle.net/ivanov11/dghm5cu7/
    return render(request, 'login.html', context)
