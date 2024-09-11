# Parcial 1

En este proyecto, desarrollarán un Sistema de Gestión de Eventos. El sistema permitirá a
los organizadores de eventos gestionar y supervisar eventos a lo largo del tiempo. Los estudiantes
deberán implementar varias funcionalidades clave para manejar la creación, edición y visualización
de eventos, así como la gestión de organizadores, utilizando relaciones entre modelos, formularios
personalizados y vistas basadas en clases.

Funcionalidades principales:

1. Gestión de Organizadores:
   • Crear organizadores que podrán gestionar múltiples eventos.
   • Listar todos los organizadores registrados.
2. Gestión de Eventos:
   • Crear, listar y editar eventos asociados a los organizadores.
   • Validar los datos del evento, asegurando que los nombres no contengan ciertas palabras
   restringidas.
3. Autenticación de Usuarios:
   • Protege ciertas vistas sensibles, como la edición de eventos, asegurando que solo los
   usuarios autenticados puedan acceder.
   Objetivos del proyecto:
   • Aplicar conceptos básicos y avanzados de Django, como modelos, formularios y vistas basadas
   en clases.
   • Implementar relaciones entre modelos (uno a muchos).
   • Usar formularios de Django con validaciones personalizadas.
   • Proteger vistas utilizando el sistema de autenticación de Django.

# Tecnologías

- Django 5.1
- Python 3.12.4

# Instalación

1. Descargar o bajar el repositorio

2. Instalar librería básicas:
   • pip install django pillow django-ckeditor

3. Ingresar en cmd o cualquier interprete de comandos:
   • cd .\"Ubicación del repositorio"\...\"Carpeta del repositorio y donde se encuentra manage.py"
   • python manage.py runserver

4. Realizar las misgraciones
   • python manage.py makemigrations
   • python manage.py migrate

# Estructura del proyecto

MiGestorEventos/
├── manage.py
├── MiGestorEventos/
│ ├── **init**.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ ├── asgi.py
│ ├── **pycache**/
│ │ ├── ...
├── eventos/
│ ├── **pycache**/
│ │ ├── ...
│ ├── **migrations**/
│ │ ├── ...
│ ├── **templates**/
│ │ ├── añadir_organizadores.html
│ │ ├── crear_evento.html
│ │ ├── editar_eventos.html
│ │ ├── editar_organizadores.html
│ │ ├── eliminar_eventos.html
│ │ ├── eliminar_organizadores.html
│ │ ├── lista_eventos.html
│ │ ├── lista_organizadores.html
│ │ ├── login.html
│ │ ├── menu_principal.html
│ │ ├── registro_login.html
│ ├── **init**.py
│ ├── admin.py
│ ├── urls.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── views.py
├── static/
│ │ ├── ...
├── mediafiles/
│ │ ├── ...
