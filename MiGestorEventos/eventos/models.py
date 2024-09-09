from django.db import models

#Modelo del Organizador
class organizador(models.Model):
    nombre_org = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_org

#Modelo del Evento
class evento(models.Model):
    nombre_event = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    organizador_relacion = models.ForeignKey(organizador, on_delete = models.CASCADE)