from django.db import models

#Modelo Organizador
class organizador(models.Model):
    nombre_org = models.CharField(max_length=100)

#Modelo Evento
class evento(models.Model):
    nombre_event = models.CharField(max_length=100)
    fecha = models.DateField(auto_created=True)
    organizador_relacion = models.ForeignKey(organizador, on_delete = models.CASCADE)