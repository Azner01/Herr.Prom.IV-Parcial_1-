from django.urls import path
from .views import *

app_name = "eventos"

urlpatterns = [
    path("home", pagina_principal, name = "pagina_principal"),
    path("eventos/", lista_eventos, name = "lista_Eventos"),
    path("eventos/crear", crear_eventos, name = "crear_Eventos"),
    path('eventos/editar/<pk>/', editar_evento.as_view(), name = "editar_Eventos"),
    path("organizadores/", organizador_lista.as_view(), name = "lista_organizadores"),
    path("organizadores/crear", organizador_añadir.as_view(), name = "añadir_organizadores"),
    path("login/registro", pagina_registro, name = "pagina_registro"),
    path("login/", pagina_login, name = "pagina_login"),

]