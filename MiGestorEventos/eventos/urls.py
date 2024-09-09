from django.urls import path
from .views import lista_eventos, crear_eventos, organizador_lista, organizador_añadir

app_name = "eventos"

urlpatterns = [
    path("eventos/", lista_eventos, name = "lista_Eventos"),
    path("eventos/crear", crear_eventos, name = "crear_Eventos"),
    path("organizadores/", organizador_lista.as_view(), name = "lista_organizadores"),
    path("organizadores/crear", organizador_añadir.as_view(), name = "añadir_organizadores"),

]