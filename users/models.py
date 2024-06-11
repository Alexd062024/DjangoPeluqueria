from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    observacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cliente.nombre} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"