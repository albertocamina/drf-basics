from django.db.models import fields
from rest_framework import serializers, viewsets

from recetas.models import *

class IngredienteSerializer( serializers.ModelSerializer ):
    
    class Meta:
        model           = Ingrediente
        fields          = "__all__"
        extra_kwargs    = {
            "nombre": {
                "trim_whitespace": True
            }
        }
        
    def validate_calorias(self, value):
        """ Funcion para validar que calorias nunca es mayor de 1000 """
        if int( value ) > 1000:
            raise serializers.ValidationError("Un ingrediente no puede tener más de 1000 calorias")

        return value


class TipoRecetaSerializer( serializers.ModelSerializer ):

    # Añadimos un nuevo campo
    numero_recetas = serializers.IntegerField( default=0 )

    class Meta: 
        model   = TipoReceta
        fields  = [ "id", "nombre", "numero_recetas" ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Contamos el numero de recetas para dicho tipo que existe
        numero_recetas = Receta.objects.filter( tipo=data.get('id', None ) ).count()

        # Lo añadimos al diccionario
        data["numero_recetas"] = numero_recetas


        return data


class RecetaSerializer( serializers.ModelSerializer ):
    # Con esto, ya pasamos el serializador para el campo de los ingredientes
    ingredientes = IngredienteSerializer( many=True )
    tipo         = TipoRecetaSerializer()

    class Meta:
        model   = Receta
        fields  = "__all__"

class FotografiaRecetaSerializer( serializers.ModelSerializer ):

    class Meta:
        model               = Receta
        fields              = [ "id", "imagen" ]
        readonly_field      = [ "id" ]
