from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import generics, mixins

from recetas.models import *
from recetas.serializers import *

class IngredientesView( generics.ListCreateAPIView ):
    """ Vista para poder listar y crear ingredientes """

    model               = Ingrediente
    serializer_class    = IngredienteSerializer
    queryset            = Ingrediente.objects.all()

class IngredienteDeleteView( generics.DestroyAPIView ):
    """ Vista para borrar ingredientes """

    model               = Ingrediente
    queryset            = Ingrediente.objects.all()

class RecetasViewSet( ModelViewSet ):
    """ Vista basada en un ViewSet de modelos para recuperar todas las recetas """

    model               = Receta
    serializer_class    = RecetaSerializer
    queryset            = Receta.objects.all() 
    allowed_methods     = ["POST"]





