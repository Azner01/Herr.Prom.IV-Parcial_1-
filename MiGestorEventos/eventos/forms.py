from django import forms
from django.core.exceptions import ValidationError

class formularioEvento(forms.ModelForm):
    nombre_evento = forms.CharField(label="Nombre del Evento",max_length=100)
    def val_nombre(self):
        nombre = self.cleaned_data['nombre']
        if "Cancelado" in nombre:
            raise ValidationError("El nombre del evento no puede contener la palabra 'Cancelado'.")
        return nombre