from django.db.models.query import QuerySet
from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework import generics, mixins, permissions

from recetas.models import *
from recetas.serializers import *
from auth_methods.permissions import WhiteListPermission, BlackListPermission

### Vista basada en funciones para poder crear los tipos de 

##############################################################################
##############################################################################
##############################################################################

### Modo con Generics donde solo hay una lista y un destroy ###

class IngredientesView( generics.ListCreateAPIView ):
    """ Vista para poder listar y crear ingredientes. Solo admite los GET en modo lista y el CREATE """

    model               = Ingrediente
    serializer_class    = IngredienteSerializer
    queryset            = Ingrediente.objects.all()

class IngredienteDeleteView( generics.DestroyAPIView ):
    """ Vista para borrar ingredientes. Solo admite los DELETE """

    model               = Ingrediente
    queryset            = Ingrediente.objects.all()

##############################################################################
##############################################################################
##############################################################################

### Vista basada en ViewSete pero con los Methods camiados para solo hacer algunas acciones ###

class IngredientesPrivateViewSet(   mixins.DestroyModelMixin,
                                    mixins.UpdateModelMixin,
                                    GenericViewSet ):
    """ 
        Vista basada en un ViewSet de modelos donde solo se puede hacer un DELETE o un PUT, pero no GET ni POST. Esto se hace gracias al 
        mixin de destroy y al de update, seguido del generic view set para poder generar los metodos necesarios.
    """

    model               = Ingrediente
    serializer_class    = IngredienteSerializer
    queryset            = Ingrediente.objects.all() 

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

##############################################################################
##############################################################################
##############################################################################

### Vista ReadOnly para un uso publico donde solo se puede hacer GET a la lista o al detail ### 

class IngredientesPublicViewSet( ReadOnlyModelViewSet ):

    model               = Ingrediente
    serializer_class    = IngredienteSerializer
    queryset            = Ingrediente.objects.all()
    # Solo se puede acceder si estas en la lista blanca y no en la lista negra
    permission_classes  = [ WhiteListPermission, BlackListPermission ]

##############################################################################
##############################################################################
##############################################################################

# Vistas para recetas con un ModelViewSet completisimo #

class RecetasViewSet( ModelViewSet ):
    """ Vista basada en un ViewSet de modelos de recetas completo """

    model               = Receta
    serializer_class    = RecetaSerializer
    queryset            = Receta.objects.all() 

##############################################################################
##############################################################################
##############################################################################





