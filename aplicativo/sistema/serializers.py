from rest_framework import serializers
from .models import ProductosModel

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosModel
        fields = '__all__'