from django.urls import path
from .views import lista_eventos, crear_eventos

app_name = "eventos"

urlpatterns = [
    path("lista_eventos/", lista_eventos, name = "lista_Eventos"),
    path("crear_eventos/", crear_eventos, name = "crear_Eventos"),
]