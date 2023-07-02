from django.urls import path
from . import views
from .views import Login, gestionsolicitudes, inicio, exit

urlpatterns = [
    path('', views.gestion),
    path('RegistrarSolicitud/', views.RegistrarSolicitud),
    path('editarSolicitud/<Id>', views.editarSolicitud),
    path('edicionSolicitud/<Id>', views.edicionSolicitud),
    path('eliminarSolicitud/<Id>', views.eliminarSolicitud),
    path('RegistrarSolicitud/', views.RegistrarSolicitud),
    path('editarSolicitud/<Id>', views.editarSolicitud),
    path('edicionSolicitud/<Id>', views.edicionSolicitud),
    path('eliminarSolicitud/<Id>', views.eliminarSolicitud),
    path('home', views.home),
    path('Bebedero', views.Bebedero),
    path('Collar', views.Collar),
    path('Comida_Gato', views.Comida_Gato),
    path('Comida_Perro', views.Comida_Perro),
    path('Contacto', views.Contacto),
    path('Fundaciones', views.Fundaciones),
    path('Nosotros', views.Nosotros),
    path('Registro', views.Registro),
    path('Tienda_subseccion_accesorios', views.Tienda_subseccion_accesorios),
    path('Tienda_subseccion_alimentos', views.Tienda_subseccion_alimentos),
    path('Tienda', views.Tienda), 
    path('', Login, name='Login'),
    path('inicio/', inicio, name='inicio'),
    path('gestionsolicitudes/', gestionsolicitudes, name = 'gestionsolicitudes'),
    path('logout/', exit, name='exit'),
]
