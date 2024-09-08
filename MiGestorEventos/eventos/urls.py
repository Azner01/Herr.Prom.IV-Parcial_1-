from django.urls import path
from . import views

app_name = "eventos"

urlpatterns = [
    path("lista_eventos/", views.lista_eventos, name = "lista_Eventos"),
]