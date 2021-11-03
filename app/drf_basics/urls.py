"""drf_basics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include

from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('admin/', admin.site.urls),

    
    path( 'recetario/', include("recetas.urls") ),
    path( 'auth/', include("auth_methods.urls") ),

    # URLS para OAuth
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # Generador de Esquemas de API
    path('openapi', get_schema_view(
        title="Django Rest Framework Bascis",
        description="API for testing basics elementos from Django Rest Framework",
        version="1.0.0"
    ), name='openapi-schema'),

   # Template view para poder cargar la vista en swagger 
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
