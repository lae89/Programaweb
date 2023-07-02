from django.urls import path
from . import views
from .views import Login, gestionsolicitudes, inicio, exit

urlpatterns = [
    path('', views.gestion),
    path('RegistrarSolicitud/', views.RegistrarSolicitud),
    path('editarSolicitud/<Id>', views.editarSolicitud),
    path('edicionSolicitud/<Id>', views.edicionSolicitud),
    path('eliminarSolicitud/<Id>', views.eliminarSolicitud), 
    path('', Login, name='Login'),
    path('inicio/', inicio, name='inicio'),
    path('gestionsolicitudes/', gestionsolicitudes, name = 'gestionsolicitudes'),
    path('logout/', exit, name='exit'),
]
