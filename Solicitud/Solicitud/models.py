from django.db import models

# Create your models here.

class Solicitud(models.Model):
    Id = models.CharField(primary_key=True, max_length=6)
    Nombre = models.CharField(max_length=50)
    Codigo = models.PositiveSmallIntegerField()