from django.shortcuts import render
from .models import evento
from .forms import formularioEvento
from django.http import HttpResponse

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

def lista_eventos(request):
    eventos = evento.objects.all()
    nom_eventos = evento.nombre_event 
    fech_eventos = evento.fecha 
    org_eventos = evento.organizador_relacion
    documento = """<html>
    <body>
    <h3> Lista de Eventos</h3>
    <h1> %s %s %s </h1>
    </body>
    <html>""" % (nom_eventos, fech_eventos, org_eventos)
    return HttpResponse(documento)

def crear_eventos(request):
    if request.method == 'POST':
        print(request.POST)
        form = formularioEvento(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = formularioEvento()
    return render(request, 'crear_evento.html', {'form': form})