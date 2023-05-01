from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import *
from .serializers import *
from django.db import transaction
from cloudinary import uploader

# Create your views here.
class CategoriasView(generics.ListCreateAPIView):
    #queryset = CategoriasModel.objects.all()
    #serializer_class = CategoriasSerializer
    def get(self, request: Request):
        categorias = CategoriasModel.objects.all()

        data_serializada = CategoriasSerializer(instance=categorias, many=True)

        return Response(data={
            'content': data_serializada.data
        })
            
        
    def post(self, request: Request):
        data = request.data
        data_serializada = CategoriasSerializer(data=data)

        resultado = data_serializada.is_valid()
        if resultado:

            nueva_categoria = CategoriasModel(**data_serializada.validated_data)
            nueva_categoria.save()

            return Response(data={
                'message': 'Categoría creada exitosamente'
            })
        else:
            return Response(data={
                'message': 'Error al crear la categoria',
                'content': data_serializada.errors
            })
        
class CategoriaView(generics.RetrieveUpdateDestroyAPIView):

    def get(self, request:Request, id):
        categoria_encontrada = CategoriasModel.objects.filter(id = id).first()

        if not categoria_encontrada:
            return Response (data={
                'message': 'categoria no existe'
            })
        resultado = CategoriasSerializer(instance=categoria_encontrada)

        return Response(data={
            'content': resultado.data
            })
    
    def put(self, request:Request, id):
        categoria_encontrada =CategoriasModel.objects.filter(id = id).first()

        if not categoria_encontrada:
            return Response(data={
                'message': 'Categoria no existe'
            })
        
        data = request.data
        data_serializada = CategoriasSerializer(data=data)

        if data_serializada.is_valid():
            categoria_encontrada.nombre = data_serializada.validated_data.get('nombre')
            categoria_encontrada.estado = data_serializada.validated_data.get('estado')

            categoria_encontrada.save()

            return Response(data={
                'message': 'Categoria actualizada'
            })
        else:
            return Response(data={
                'message': 'Error al actualizar la categoría',
                'content': data_serializada.errors
            })

    def delete(self, request: Request, id):
        categoria_encontrada = CategoriasModel.objects.filter(id = id).first()
        
        if not categoria_encontrada:
            return Response(data={
                'message': 'categoria no existe'
            }, status=404)
        
        resultado = CategoriasModel.objects.filter(id = id).delete()
        print(resultado)

        return Response(data={
            'message': 'Categoria eliminada exitosamente'
        })

class ProductosView(generics.ListCreateAPIView):
    def post(self, request:Request):
        try:
            data = {
                'nombre': request.data.get('nombre'),
                'descripcion': request.data.get('descripcion'),
                'foto': request.FILES.get('foto'),
                'precio': request.data.get('precio'),
                'estado': request.data.get('estado'),
            }
            serializador = ProductosSerializer(data=data)
            if serializador.is_valid():
                serializador.save()

                return Response(data={
                        'message': 'Producto creado exitosamente',
                        'content': resultado.data
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response (data={
                    'message': 'Error al crear el producto',
                    'content': data_serializada.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={
                'message': 'Error al crear el producto',
                'content': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request: Request):

        #total_productos = ProductosModel.objects.count()
        productos = ProductosModel.objects.all()[skip:take]

        #informacion_paginacion = paginationSerializer(total_productos, page, perPage)
        data_serializada = ProductosSerializer(instance=productos, many=True)
        
        return Response(data={
            'content': data_serializada.data,
        }, status=status.HTTP_200_OK)

class ProductoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductosModel.objects.all()
    serializer_class = ProductosSerializer

class PagosView(generics.ListCreateAPIView):
    queryset = PagosModel.objects.all()
    serializer_class = PagosSerializer

class PagoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PagosModel.objects.all()
    serializer_class = PagosSerializer

    def delete(self, request, pk):
        self.serializer_class(self.get_queryset().get(id=pk)).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VentasView(generics.ListCreateAPIView):
    queryset = VentasModel.objects.all()
    serializer_class = VentasSerializer

    @transaction.atomic
    def post(self, request):
        try:
            cliente = ClientesModel(
                nombre=request.data['cliente']['nombre'],
                correo=request.data['cliente']['correo'],
                dni=request.data['cliente']['dni'],
            )
            cliente.save()

            usuario = User.objects.get(id=request.data['usuario_id'])
            venta = VentasModel(
                observacion=request.data['observacion'],
                usuario_id=usuario,
                cliente_id=cliente,
            )
            venta.save()

            for detalle in request.data['detalles_venta']:
                producto = ProductosModel.objects.get(id=detalle['producto_id'])
                detalle = DetallesVentaModel(
                    cantidad=detalle['cantidad'],
                    producto_id=producto,
                    venta_id=venta,
                )
                detalle.save()
            return Response({
                'message': 'Venta registrada correctamente'
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)