from django.conf.urls import url
from login.views import *


urlpatterns = [
    url(r'^$', Viewlogin.as_view(), name="login"),
    url(r'^login', Viewlogin.as_view(), name="login"),
    url(r'^logout', Logout.as_view(),  name="logout"), 
]
