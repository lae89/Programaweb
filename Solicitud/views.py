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

def home(request):
    Inicio = Inicio.objects.all()
    return render(request, "Inicio.html")

def Bebedero(request):
    Inicio = Bebedero.objects.all()
    return render(request, "Bebedero.html")

def Collar(request):
    Inicio = Collar.objects.all()
    return render(request, "Collar.html")

def Comida_Gato(request):
    Comida_Gato = Comida_Gato.objects.all()
    return render(request, "Comida Gato.html")

def Comida_Perro(request):
    Comida_Perro = Comida_Perro.objects.all()
    return render(request, "Comida_Perro.html")

def Contacto(request):
    Contacto = Contacto.objects.all()
    return render(request, "Contacto.html")

def Fundaciones(request):
    Fundaciones = Fundaciones.objects.all()
    return render(request, "Fundaciones.html")

def Nosotros(request):
    Nosotros = Nosotros.objects.all()
    return render(request, "Nosotros.html")

def Registro(request):
    Registro = Registro.objects.all()
    return render(request, "Registro.html")

def Tienda_subseccion_accesorios(request):
    Tienda_subseccion_accesorios = Tienda_subseccion_accesorios.objects.all()
    return render(request, "Tienda subseccion accesorios.html")

def Tienda_subseccion_alimentos(request):
    Tienda_subseccion_alimentos = Tienda_subseccion_alimentos.objects.all()
    return render(request, "Tienda subseccion alimentos.html")

def Tienda(request):
    Tienda = Tienda.objects.all()
    return render(request, "Tienda.html")