from django.urls import path
from .views import *

urlpatterns = [
        path('categorias', CategoriasView.as_view()),
        path('categorias/<int:id>', CategoriaView.as_view()),
        path('productos', ProductosView.as_view()),
        path('productos/<int:id>', ProductoView.as_view()),
        path('pagos', PagosView.as_view()),
        path('pagos/<int:pk>', PagoView.as_view()),
        path('ventas', VentasView.as_view())
]