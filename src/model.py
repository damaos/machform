from django.db import models
from django.contrib.auth.models import User
from ipware.ip import get_ip
from django.utils.deprecation import MiddlewareMixin

from src.middleware import current_request
from src.middleware import *
#from src.manager import CustomManager


class BaseModel(models.Model):
   
    # Datos que estan incluidos en la base de datos y que son necesarios para cada modelo

    created_at = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha ultima de modificación', auto_now=True)
    created_by = models.ForeignKey(User, verbose_name='Creado por', related_name='%(app_label)s_%(class)s_created_by')
    updated_by = models.ForeignKey(User, verbose_name='Ultima modificación por', related_name='%(app_label)s_%(class)s_updated_by')
    ip_forwarded = models.CharField(verbose_name='Ip de modificación', max_length=50)
    
    #deleted = models.BooleanField('Eliminado', default=False)
    
    # objects = CustomManager()
        
    # def delete(self):
        
    #     self.deleted = True
    #     self.save()
    #Get ip address User
    def get_client_ip(self, request):
        
        x_forwarded_for = request.current_request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.current_request.META.get('REMOTE_ADDR')
        return ip

    def save(self, *args, **kwargs):
        

        request = current_request()
        #verificar si esta haciendo add or update
        if self._state.adding:
            self.created_by = request.current_request.user
            self.updated_by = request.current_request.user
        else:
            self.updated_by = request.current_request.user

            self.ip_forwarded = self.get_client_ip(request)
            

        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        