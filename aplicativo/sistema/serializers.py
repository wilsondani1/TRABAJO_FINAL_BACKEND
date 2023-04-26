from rest_framework.serializers import ModelSerializer
from .models import *


class CategoriasSerializer(ModelSerializer):
    class Meta:
        model = CategoriasModel
        fields = '__all__'
    
    def delete(self):
        self.instance.estado = False
        self.instance.save()
        return self.instance

class ProductosSerializer(ModelSerializer):
    class Meta:
        model = ProductosModel
        fields = '__all__'

class ClientesSerializer(ModelSerializer):
    class Meta:
        model = ClientesModel
        fields = '__all__'

class DetallesVentaSerializer(ModelSerializer):
    class Meta:
        model = DetallesVentaModel
        fields = '__all__'

class VentasSerializer(ModelSerializer):
    cliente = ClientesSerializer()
    detalle_venta = DetallesVentaSerializer(many=True)
    class Meta:
        model = VentasModel
        fields = '__all__'


class PagosSerializer(ModelSerializer):
    class Meta:
        model = PagosModel
        fields = '__all__'

    def delete(self):
        self.instance.estado = False
        self.instance.save()
        return self.instance