from django.shortcuts import render, redirect
from .models import Solicitud
from django.contrib import messages

# Create your views here.

def gestion(request):
    listaSolicitudes = Solicitud.objects.all()
    messages.success(request, '¡Solicitudes listadas!')
    return render(request, "gestionsolicitudes.html", {"solicitudes": listaSolicitudes})

def RegistrarSolicitud(request):
    Id=request.POST['txtId']
    Nombre_solicitud=request.POST['txtNombre_solicitud']
    Mensaje=request.POST['txtMensaje']

    solicitud = Solicitud.objects.create(Id=Id, Nombre_solicitud=Nombre_solicitud, Mensaje=Mensaje)
    messages.success(request, '¡Solicitud registrada!')
    return redirect('/')

def editarSolicitud(request, Id):
    solicitud = Solicitud.objects.get(Id=Id)
    return render(request, "editarsolicitud.html", {"solicitud: solicitud"})

def edicionSolicitud(request):
    Id=request.POST['txtId']
    Nombre_solicitud=request.POST['txtNombre_solicitud']
    Mensaje=request.POST['txtMensaje']

    solicitud = Solicitud.objects.get(Id=Id)
    solicitud.Nombre_solicitud = Nombre_solicitud
    solicitud.Mensaje = Mensaje
    solicitud.save()
    messages.success(request, '¡Solicitud modificada!')

    return redirect('/')

def eliminarSolicitud(request, Id):
    solicitud = Solicitud.objects.get(Id=Id)
    solicitud.delete()

    messages.success(request, '¡Solicitud eliminada!')
    return redirect('/')