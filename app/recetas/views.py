from django.contrib import auth
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import status

from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import generics, mixins, permissions
from rest_framework.throttling import AnonRateThrottle
from rest_framework.authentication import *
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.renderers import TemplateHTMLRenderer
from auth_methods.permissions import WhiteListPermission, BlackListPermission

from rest_framework_simplejwt.authentication import JWTAuthentication


from recetas.models import *
from recetas.serializers import *
from recetas.filters import *



### Vista basada en funciones para poder crear los tipos de recetas ### 

@api_view(['GET'])
@authentication_classes([ JWTAuthentication ])
@permission_classes([ IsAuthenticated ])
def API_get_tipo_recetas( request ):
    """ Funcion para recuperar los tipos de recetas existentes """

    # Cogemos todos los tipos de recetas
    tipos_recetas = TipoReceta.objects.all()

    # Cogemos el serializador
    tipos_recetas_ser = TipoRecetaSerializer( tipos_recetas, many=True )
    
    return Response( tipos_recetas_ser.data, status=HTTP_200_OK )


##############################################################################
##############################################################################
##############################################################################

### Modo con Generics donde solo hay una lista y un destroy ###

class IngredientesView( generics.ListCreateAPIView ):
    """ Vista para poder listar y crear ingredientes. Solo admite los GET en modo lista y el CREATE """

    model                   = Ingrediente
    serializer_class        = IngredienteSerializer
    queryset                = Ingrediente.objects.all()
    throttle_classes        = [AnonRateThrottle]
    authentication_classes  = [ BasicAuthentication ]
    permission_classes      = [ IsAuthenticated ]

    search_fields           = ["nombre", "calorias"]
    ordering_fields         = ["nombre"]
    filterset_fields        = [ "id" ]


    ### Más info ### 
    # Para la autentificación básica, se mandas credenciales de usuario en las cabeceras HTTP, 
    # Recomendable usar HTTPS para este método o no será seguro

    # Se debe mandar un header: Authorization Basic {base64 data}
    # Donde la parte en Base64 es {username}:{password}


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

    model                   = Ingrediente
    serializer_class        = IngredienteSerializer
    queryset                = Ingrediente.objects.all() 


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
    """ Vista basada en un ViewSet de modelos de recetas completo 

        El modo de autentificacion y permisos es para un usuario por Token asignado

    """

    model                   = Receta
    serializer_class        = RecetaSerializer
    queryset                = Receta.objects.all() 
    authentication_classes  = [ TokenAuthentication ]
    permission_classes      = [ IsAuthenticated ]

    filterset_class         = RecetasFilterSet

    def get_serializer_class(self):

        if self.action == "upload_imagen":
            return FotografiaRecetaSerializer

        return super().get_serializer_class()

    @action( methods=["POST"], detail=True, url_path="upload-imagen")
    def upload_imagen( self, request, pk=None ):
        """ Acción para subir una imagen """

        # Cogemos la receta necesaria
        receta = self.get_object()
        # Serializamos los datos que llegan
        serializer = self.get_serializer(
            receta,
            data=request.data
        )

        # Comprobamos que sea correcta
        if serializer.is_valid():
            serializer.save()

            return Response( 
                serializer.data,
                status=HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )


class RecetasViewSetHTML( ModelViewSet ):
    """ Vista basada en un ViewSet de modelos de recetas completo 

        El modo de autentificacion y permisos es para un usuario por Token asignado

    """

    model                   = Receta
    serializer_class        = RecetaSerializer
    queryset                = Receta.objects.all() 
    authentication_classes  = [ TokenAuthentication ]
    permission_classes      = [ IsAuthenticated ]

    # Decimos que la clase para renderizar es un HTML
    renderer_classes        = [ TemplateHTMLRenderer ]
    template_name           = "recetas.html"
    
    filterset_class         = RecetasFilterSet



##############################################################################
##############################################################################
##############################################################################

### Vista para crear los Deseos ### 



##############################################################################
##############################################################################
##############################################################################




