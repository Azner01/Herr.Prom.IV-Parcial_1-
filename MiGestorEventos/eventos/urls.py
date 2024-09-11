from django.urls import path
from .views import *

app_name = "eventos"

urlpatterns = [
    path("home", pagina_principal, name = "pagina_principal"),
    path("eventos/", lista_eventos.as_view(), name = "lista_Eventos"),
    path("eventos/crear", crear_eventos, name = "crear_Eventos"),
    path('eventos/editar/<int:pk>/', login_required(editar_evento.as_view(), login_url='/gestor_eventos/login/'), name = "editar_Eventos"),
    path('eventos/borrar/<int:pk>/', eliminar_evento.as_view(), name = "borrar_Eventos"),
    path("organizadores/", organizador_lista.as_view(), name = "lista_organizadores"),
    path("organizadores/crear", organizador_añadir.as_view(), name = "añadir_organizadores"),
    path('organizadores/editar/<int:pk>/', organizador_editar.as_view(), name = "editar_organizador"),
    path('organizadores/borrar/<int:pk>/', organizador_eliminar.as_view(), name = "borrar_organizador"),
    path("login/registro", pagina_registro, name = "pagina_registro"),
    path("login/", pagina_login, name = "pagina_login"),

]