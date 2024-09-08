from django.shortcuts import render
from .models import evento

def lista_eventos(request):
    eventos = evento.objects.all()
    return render(request, 'index.html')