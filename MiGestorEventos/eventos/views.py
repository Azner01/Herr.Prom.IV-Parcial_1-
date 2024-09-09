from django.shortcuts import render
from .models import evento, organizador
from .forms import formularioEvento
# from django.http import HttpResponse
# from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

def lista_eventos(request):
    eventos = evento.objects.all()
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def crear_eventos(request):
    if request.method == 'POST':
        print(request.POST)
        form = formularioEvento(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = formularioEvento()
    return render(request, 'crear_evento.html', {'form': form})


class organizador_lista(ListView):
    model = organizador
    template_name = 'lista_organizadores.html'

class organizador_añadir(CreateView):
    model = organizador
    fields = ['nombre_org']
    template_name = 'añadir_organizadores.html'
    success_url = '/eventos/organizadores/'