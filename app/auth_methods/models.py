from django.db import models

class WhiteList( models.Model ):
    host = models.CharField( max_length=255, blank=False, null=False )

class BlackList( models.Model ):
    host = models.CharField( max_length=255, blank=False, null=False )
