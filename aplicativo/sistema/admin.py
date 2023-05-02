from django.contrib import admin
from .models import ProductosModel
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
  list_display = ('id', 'nombre', 'descripcion', 'precio', 'foto', 'estado')

admin.site.register(ProductosModel, MyModelAdmin)
