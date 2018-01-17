"""machform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.contrib import admin
from inventory.views import first_view
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),


    url(r'^', include('login.urls', namespace='login', app_name='login')),
    url(r'^login/', include('login.urls', namespace='login', app_name='login')),


    url(r'^machform/', include('inventory.urls', namespace='inventory', app_name='inventory')),
    

    url(r'^reset/password', auth_views.password_reset, {'template_name':'registration/password_reset_form.html',
        'email_template_name':'registration/password_reset_email.html'}, name='password_reset'),
    url(r'^reset/password/done', auth_views.password_reset_done, {'template_name':'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/', auth_views.password_reset_confirm, {'template_name':'registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done', auth_views.password_reset_complete, {'template_name':'registration/password_reset_complete.html'}, name='password_reset_complete'),


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns