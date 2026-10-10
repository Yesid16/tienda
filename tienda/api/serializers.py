from rest_framework import serializers
from tienda.models import Libro


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'precio', 'stock_actual']


class OrdenInputSerializer(serializers.Serializer):
    """Valida la entrada de datos (actúa como DTO)."""
    libro_id = serializers.IntegerField()
    direccion_envio = serializers.CharField(max_length=200)