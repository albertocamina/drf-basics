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

class RecetaSerializer( serializers.ModelSerializer ):

    class Meta:
        model   = Receta
        fields  = "__all__"