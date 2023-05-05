from rest_framework.serializers import ModelSerializer
from .models import *

class RegistroUsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class Personserializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'tipoUsuario']

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
    
    def to_representation(self, instance):
        representacion = super().to_representation(instance)
        representacion['foto'] = instance.foto.url
        return representacion

# class ClientesSerializer(ModelSerializer):
#     class Meta:
#         model = ClientesModel
#         fields = '__all__'

# class DetallesVentaSerializer(ModelSerializer):
#     class Meta:
#         model = DetallesVentaModel
#         fields = '__all__'
#         extra_kwargs = {
#             'venta_id': {'read_only': True},
#         }

# class VentasSerializer(ModelSerializer):
#     cliente = ClientesSerializer(source='cliente_id')
#     detalles_venta = DetallesVentaSerializer(source='detallesVenta', many=True)
#     class Meta:
#         model = VentasModel
#         fields = '__all__'
#         extra_kwargs = {
#             'cliente_id': {'read_only': True},
#         }

# class PagosSerializer(ModelSerializer):
#     class Meta:
#         model = PagosModel
#         fields = '__all__'

#     def delete(self):
#         self.instance.estado = False
#         self.instance.save()
#         return self.instance