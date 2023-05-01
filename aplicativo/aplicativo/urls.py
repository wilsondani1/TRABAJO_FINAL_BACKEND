"""
URL configuration for aplicativo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
openapi.Info(
    title="Snippets API",
    default_version='v1',
    description="Test description",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="contact@snippets.local"),
    license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=[permissions.AllowAny],
)

# https://coffeebytes.dev/django-rest-framework-y-jwt-para-autenticar-usuarios/


urlpatterns = [
    path('swagger/',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/',schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/',admin.site.urls),
    path('sistema/', include('sistema.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
