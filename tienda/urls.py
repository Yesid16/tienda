from django.urls import path
from .views import CompraView, inventario
from .api.views import CompraAPIView, ProductoListAPIView

urlpatterns = [
    path("comprar/", CompraView.as_view(), name="comprar"),
    path("inventario/", inventario, name="inventario"),
    path("api/v1/comprar/", CompraAPIView.as_view(), name="api_comprar"),
    path("api/v1/productos/", ProductoListAPIView.as_view(), name="api_productos"),
]