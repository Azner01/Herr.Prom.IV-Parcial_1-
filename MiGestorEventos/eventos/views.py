from django.shortcuts import render, redirect
from .models import *
from .forms import *
# from django.http import HttpResponse
# from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import FormView
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

def pagina_principal(request):
    return render(request, 'menu_principal.html')


def lista_eventos(request):
    eventos = evento.objects.all()
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def crear_eventos(request):
    if request.method == 'POST':
        form = formularioEvento(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = formularioEvento()
    return render(request, 'crear_evento.html', {'form': form})


class organizador_lista(ListView):
    model = organizador
    template_name = 'lista_organizadores.html'
    success_url = '/gestor_eventos/eventos/crear/'

class organizador_añadir(CreateView):
    model = organizador
    fields = ['nombre_org']
    template_name = 'añadir_organizadores.html'
    success_url = '/gestor_eventos/organizadores/'

# class editar_eventos(ListView):
#     model = evento
#     template_name = 'editar_eventos.html'

class editar_evento(UpdateView):
    model = evento
    form_class = formularioEvento
    template_name = 'editar_evento.html'
    success_url ="/"


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
    context = {}
    #Diseño de la página obtenido: https://jsfiddle.net/ivanov11/dghm5cu7/
    return render(request, 'login.html', context)
