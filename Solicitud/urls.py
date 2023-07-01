from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestion),
    path('RegistrarSolicitud/', views.RegistrarSolicitud),
    path('editarSolicitud/<Id>', views.editarSolicitud),
    path('edicionSolicitud/<Id>', views.edicionSolicitud),
    path('eliminarSolicitud/<Id>', views.eliminarSolicitud)
]
