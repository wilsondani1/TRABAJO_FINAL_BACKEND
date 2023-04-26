from django.db import models

class ProductosModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    imagen_url = models.TextField()
    precio = models.FloatField()
    estado = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = "productos"
