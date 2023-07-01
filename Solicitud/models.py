from django.db import models

# Create your models here.

class Solicitud(models.Model):
    Id = models.CharField(primary_key=True, max_length=6)
    Nombre_solicitud = models.CharField(max_length=50)
    Mensaje = models.CharField(max_length=5000)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.Nombre_solicitud)