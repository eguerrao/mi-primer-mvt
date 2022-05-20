from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from sys import maxsize
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10, default="Femenino")
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fono = models.IntegerField(default=0, blank=True, null=True)
