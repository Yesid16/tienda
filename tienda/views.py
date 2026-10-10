from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views import View
from .domain.models import Libro
from .domain.models import Producto
from .infra.factories import PaymentFactory
from .services import CompraService


class CompraView(View):
    def setup_service(self):
        gateway = PaymentFactory.get_processor()
        return CompraService(procesador_pago=gateway)

    def get(self, request):
        User = get_user_model()
        usuario, _ = User.objects.get_or_create(username="demo")
        producto, _ = Producto.objects.get_or_create(
            nombre="Teclado", defaults={"precio": 100000}
        )

        servicio = self.setup_service()
        resultado = servicio.ejecutar_proceso_compra(
            usuario, [producto], "Calle 10 # 20-30, Medellín"
        )
        return HttpResponse(resultado)
def inventario(request):
    filas = "".join(
        f"<tr><td>{l.id}</td><td>{l.titulo}</td><td>{l.precio}</td><td>{l.stock_actual}</td></tr>"
        for l in Libro.objects.all()
    )
    html = (
        "<h1>Inventario</h1>"
        "<table border='1' cellpadding='6'>"
        "<tr><th>ID</th><th>Título</th><th>Precio</th><th>Stock</th></tr>"
        f"{filas}</table>"
    )
    return HttpResponse(html)