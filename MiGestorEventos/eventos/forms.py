from django import forms
from .models import evento
from django.core.exceptions import ValidationError

class formularioEvento(forms.ModelForm):
    class Meta:
        model = evento
        fields = ['nombre_event','organizador_relacion']
    def clean_nombre_event(self):
        nombre = self.cleaned_data['nombre_event']
        if "Cancelado" in nombre:
            raise forms.ValidationError("El nombre del evento no puede contener la palabra 'Cancelado'.")
        return nombre
