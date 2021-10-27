from django.conf.urls import url
from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import apply_suffix_patterns

from recetas.views import *

app_name = "recetas"

recetas_router = DefaultRouter()
recetas_router.register( r'recetas', RecetasViewSet, basename="recetas"  )


urlpatterns = [
    url( r"^ingredientes/$", IngredientesView.as_view(), name="ingredientes" ),
    url( r"^ingredientes/(?P<pk>[0-9]+)/delete$", IngredienteDeleteView.as_view(), name="ingredientes_delete" ),
]

urlpatterns += recetas_router.urls

