from django.db.models import query
from django_filters import rest_framework
from django_filters import filters

from recetas.models import *

class RecetasFilterSet(rest_framework.FilterSet):

    # Ejemplo de filtro donde siempre solo se pueden elegir ingredientes con menos de 300 calorias
    ingredientes_bajo_caloricos = filters.ModelMultipleChoiceFilter( queryset=Ingrediente.objects.filter( calorias__lte=300 ) )

    class Meta:
        model   = Receta
        fields  = ["id", "ingredientes", "tipo" ]
        


        
    