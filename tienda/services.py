from django.db import transaction

from .domain.builders import OrdenBuilder
from .domain.models import Libro


class CompraService:
    def __init__(self, procesador_pago):
        self.procesador = procesador_pago
        self.builder = OrdenBuilder()

    def ejecutar_proceso_compra(self, usuario, lista_productos, direccion):
        orden = (self.builder
                 .con_usuario(usuario)
                 .con_productos(lista_productos)
                 .para_envio(direccion)
                 .build())

        if self.procesador.pagar(orden.total):
            return f"Orden {orden.id} procesada exitosamente."

        orden.delete()
        raise Exception("Error en la pasarela de pagos.")

    def ejecutar_compra(self, libro_id, direccion, usuario):
        with transaction.atomic():
            try:
                libro = Libro.objects.get(id=libro_id)
            except Libro.DoesNotExist:
                raise ValueError("El libro no existe.")

            if libro.stock_actual < 1:
                raise ValueError("Sin stock disponible.")

            orden = (self.builder
                     .con_usuario(usuario)
                     .con_productos([libro])
                     .para_envio(direccion)
                     .build())

            if not self.procesador.pagar(orden.total):
                raise Exception("Error en la pasarela de pagos.")

            libro.stock_actual -= 1
            libro.save()

        return orden.total