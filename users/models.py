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
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.cliente.nombre} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    cantidad_disponible = models.IntegerField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    compra = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=255)
    adquisicion = models.DateField()
    marca = models.CharField(max_length=255)
    proveedor = models.CharField(max_length=255)
    notas = models.TextField(blank=True, null=True)
    codigo_barras = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre
        