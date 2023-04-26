
from rest_framework import generics
from .models import ProductosModel
from .serializers import ProductosSerializer


# Create your views here.

class ProductosView(generics.ListCreateAPIView):
    queryset = ProductosModel.objects.all()
    serializer_class = ProductosSerializer
    

class ProductoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductosModel.objects.all()
    serializer_class = ProductosSerializer


