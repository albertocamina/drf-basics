from rest_framework import permissions

from django.db.models import Q
from rest_framework.decorators import permission_classes

from auth_methods.models import WhiteList, BlackList

class WhiteListPermission( permissions.BasePermission ):
    """ Permiso de lista blanca para acceder a una vista """

    def has_permission(self, request, view):
        
        dominio     = request.META['REMOTE_HOST']
        _ip          = request.META['REMOTE_ADDR']

        return WhiteList.objects.filter(Q( host=dominio)|Q(host=_ip)).exists()

class BlackListPermission( permissions.BasePermission ):
    """ Permiso de lista blanca para acceder a una vista """

    def has_permission(self, request, view):
        
        dominio     = request.META['REMOTE_HOST']
        ip          = request.META['REMOTE_ADDR']

        return not BlackList.objects.filter(Q( host=dominio)|Q(host=ip)).exists()

class PermsClassPermission( permissions.BasePermission ):
    """ Permiso para vistas autentificadas donde queremos comprobar que el usuario tiene uno o varios Perms 
        pasados por medio de una lista. Esto es muy interesante, pues sustituye al tipo request.user.has_perms()
        repetido en todas las vistas y manda un 403 de manera basica.     
    """

    def has_permission(self, request, view):
        return request.user is not None and request.user.has_perms( view.required_perms )




