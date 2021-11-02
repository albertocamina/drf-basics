from rest_framework import permissions

from django.db.models import Q

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

