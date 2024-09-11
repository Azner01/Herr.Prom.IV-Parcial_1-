from django import forms
from .models import evento
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class formularioEvento(forms.ModelForm):
    class Meta:
        model = evento
        fields = ['nombre_event','organizador_relacion']
        labels = {
        'nombre_event': 'Nombre del Evento',
        'organizador_relacion': 'Organizador del evento',
        }
    def clean_nombre_event(self):
        nombre = self.cleaned_data['nombre_event']
        if "Cancelado" in nombre:
            raise forms.ValidationError("El nombre del evento no puede contener la palabra 'Cancelado'.")
        return nombre

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

      
    
    
