from django.conf import settings
from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre


class Orden(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    direccion_envio = models.CharField(max_length=255, blank=True)
    creada = models.DateTimeField(auto_now_add=True)

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    stock_actual = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo