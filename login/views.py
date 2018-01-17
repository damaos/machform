import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
class Viewlogin(View):
    
    template_name = 'login.html'
    
    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {})
    
    def post(self, request, *args, **kwargs):

        usuariol = request.POST.get('username')
        passwordl = request.POST.get('password')

        if usuariol and passwordl:

            info = {'user': usuariol, 'password': passwordl}
            try:
                users = User.objects.get(username=usuariol)           
            except ObjectDoesNotExist:
                messages.error(request, 'El usuario no se encuentra activo.')
                return HttpResponseRedirect(reverse('login:login')) 
            try:
                ws_response = requests.post(settings.URL_AUTHENTICATION, data=info)
                ws_response.json()
                if ws_response.status_code == requests.codes.ok:             
                    try:
                        login(request, users)
                        request.session.set_expiry(settings.SESSION_TIMEOUT)
                        return HttpResponseRedirect(reverse('inventory:index'))   
                        
                    except User.DoesNotExist:
                        user = None
                        messages.error(request, 'El usuario no se encuentra registrado en la aplicación.')                    
                        return HttpResponseRedirect(reverse('login:login'))
                
                else:
                    messages.error(request, 'Nombre de usuario o Contraseña incorrectos.')
                    return HttpResponseRedirect(reverse('login:login'))
            except Exception as e:
                messages.error(request, 'Actualmente no se puede ingresar a la aplicación por favor intente más tarde')
                return HttpResponseRedirect(reverse('login:login'))
        else:
            messages.error(request, 'Nombre de usuario y contraseña son obligatorios.')
            return HttpResponseRedirect(reverse('login:login'))

        
class Logout(View):
    '''
    Clase para finalizar la sesión.
    '''
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('login:login')) 