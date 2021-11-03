from django.db import models
from django.contrib.auth import get_user_model

class TipoReceta( models.Model ):
    nombre          = models.CharField( max_length=500, unique=True, blank=False, null=False )

class Ingrediente( models.Model ):
    nombre          = models.CharField( max_length=500, unique=True, blank=False, null=False )
    calorias        = models.PositiveIntegerField( blank=False, null=False, default=0 )

class Receta( models.Model ):
    nombre          = models.CharField( max_length=1500, unique=True, blank=False, null=False )
    tipo            = models.ForeignKey("recetas.TipoReceta", related_name="recetas", on_delete=models.PROTECT, blank=True, null=True ) 
    ingredientes    = models.ManyToManyField("recetas.Ingrediente", related_name="recetas")
    imagen          = models.ImageField(null=True)

class Deseo( models.Model ): 
    receta          = models.ForeignKey("recetas.Receta", related_name="recetas", on_delete=models.PROTECT, blank=False, null=False ) 
    usuario         = models.ForeignKey( get_user_model(), related_name="recetas", on_delete=models.PROTECT, blank=False, null=False ) 