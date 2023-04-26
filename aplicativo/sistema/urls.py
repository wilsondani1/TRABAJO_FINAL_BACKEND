from django.urls import path
from .views import *

urlpatterns = [
        path ('productos', ProductosView.as_view()),
        path ('productos/<int:pk>', ProductoView.as_view()),

]