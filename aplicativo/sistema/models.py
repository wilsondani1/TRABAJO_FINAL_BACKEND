from django.db import models
from django.contrib.auth.models import User

class CategoriasModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "categorias"

class ProductosModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    imagen_url = models.TextField()
    precio = models.FloatField()
    estado = models.BooleanField(default=True)
    categoria_id = models.ForeignKey(CategoriasModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "productos"

class ClientesModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "clientes"

class VentasModel(models.Model):
    id = models.AutoField(primary_key=True)
    observacion = models.CharField(max_length=100)
    cliente_id = models.ForeignKey(ClientesModel, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "ventas"

class DetallesVentaModel(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    producto_id = models.ForeignKey(ProductosModel, on_delete=models.CASCADE)
    venta_id = models.ForeignKey(VentasModel, on_delete=models.CASCADE, related_name='detallesVenta')

    class Meta:
        db_table = "detalles_venta"

class PagosModel(models.Model):
    id = models.AutoField(primary_key=True)
    monto = models.FloatField()
    estado = models.BooleanField(default=True)
    venta_id = models.ForeignKey(VentasModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "pagos"