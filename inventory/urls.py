from inventory.views import *
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django_filters.views import FilterView

urlpatterns = (
    
    url(r'^index', login_required(first_view.as_view()), name="index"),
    
    #url(r'^vertroncales', login_required(ver_troncales.as_view()), name="vertroncales"),
    
    url(r'^detalletroncal', login_required(trunk_info.as_view()), name="detalletroncal"),
    url(r'^detalletrunk', login_required(trunk_enla.as_view()), name="detalletrunk"),
    url(r'^detallenum', login_required(enla_dnis.as_view()), name="detallenum"),
    url(r'^detallednis', login_required(dnis_liext.as_view()), name="detallednis"),

    url(r'^registroncal', login_required(regis_troncal.as_view()), name="registroncal"),
    url(r'^(?P<pk>\d+)/editroncal', login_required(edit_troncal.as_view()), name="editroncal"),
    url(r'^elimtroncal/(?P<pk>\d+)', login_required(elim_troncal.as_view()), name='elimtroncal'),
    url(r'^addtroncal', login_required(addtrunk.as_view()), name='addtroncal'),
    
    url(r'^registroncal', login_required(regis_troncal.as_view()), name='registroncal'),
    url(r'^trunkenlacelist', login_required(trunkenlacelist.as_view()), name='trunkenlacelist'),

    url(r'^addusuario', login_required(addusuario.as_view()), name='addusuario'),
    url(r'^usuariolist', login_required(usuariolist.as_view()), name='usuariolist'),
    url(r'^usuarioeact/(?P<pk>\d+)$', login_required(usuarioeact.as_view()), name='usuarioeact'),
    url(r'^usuarioelim/(?P<pk>\d+)$', login_required(usuarioelim.as_view()), name='usuarioelim'),

    url(r'^trunkelist', login_required(trunkelist.as_view()), name='trunkelist'),
    url(r'^trunkeact/(?P<pk>\d+)$', login_required(trunkeact.as_view()), name='trunkeact'),
    url(r'^trunkelim/(?P<pk>\d+)$', login_required(trunkelim.as_view()), name='trunkelim'),
    url(r'^trunkdeta/(?P<pk>\d+)', login_required(trunkdeta.as_view()), name='trunkdeta'),

    url(r'^addlinea', login_required(addlinea.as_view()), name='addlinea'),
    url(r'^linealist', linealist.as_view(), name='linealist'),
    url(r'^lineaeact/(?P<pk>\d+)$', login_required(lineaeact.as_view()), name='lineaeact'),
    url(r'^lineaelim/(?P<pk>\d+)$', login_required(lineaelim.as_view()), name='lineaelim'),
    url(r'^lineadeta/(?P<pk>\d+)', login_required(lineadeta.as_view()), name='lineadeta'),
    
    url(r'^adddnis', login_required(adddnis.as_view()), name='adddnis'),
    url(r'^dnisaddcliente', login_required(addclientednis.as_view()), name='dnisaddcliente'),
    url(r'^dnislist', login_required(dnislist.as_view()), name='dnislist'),
    url(r'^dniseact/(?P<pk>\d+)$', login_required(dniseact.as_view()), name='dniseact'),
    url(r'^dniselim/(?P<pk>\d+)$', login_required(dniselim.as_view()), name='dniselim'),
    url(r'^dnisdeta/(?P<pk>\d+)', login_required(dnisdeta.as_view()), name='dnisdeta'),

    url(r'^addliext', login_required(addliext.as_view()), name='addliext'),
    url(r'^linextlist', login_required(linextlist.as_view()), name='linextlist'),
    url(r'^linexteact/(?P<pk>\d+)$', login_required(linexteact.as_view()), name='linexteact'),
    url(r'^linextelim/(?P<pk>\d+)$', login_required(linextelim.as_view()), name='linextelim'),
    url(r'^linextdeta/(?P<pk>\d+)', login_required(linextdeta.as_view()), name='linextdeta'),
    
    url(r'^addtiptrunk', login_required(addtiptrunk.as_view()), name='addtiptrunk'),
    url(r'^tiptrunklist', login_required(tiptrunklist.as_view()), name='tiptrunklist'),
    url(r'^tiptrunkeact/(?P<pk>\d+)$', login_required(tiptrunkeact.as_view()), name='tiptrunkeact'),
    url(r'^tiptrunkelim/(?P<pk>\d+)$', login_required(tiptrunkelim.as_view()), name='tiptrunkelim'),
    url(r'^tiptrunkdeta/(?P<pk>\d+)', login_required(tiptrunkdeta.as_view()), name='tiptrunkdeta'),

    url(r'^addcliente', login_required(addcliente.as_view()), name='addcliente'),
    url(r'^clienlist', login_required(clienlist.as_view()), name='clienlist'),
    url(r'^clieneact/(?P<pk>\d+)$', login_required(clieneact.as_view()), name='clieneact'),
    url(r'^clienelim/(?P<pk>\d+)$', login_required(clienelim.as_view()), name='clienelim'),
    url(r'^cliendeta/(?P<pk>\d+)', login_required(cliendeta.as_view()), name='cliendeta'),

    url(r'^addsede', login_required(addsede.as_view()), name='addsede'),
    url(r'^sedelist', login_required(sedelist.as_view()), name='sedelist'),
    url(r'^sedeeact/(?P<pk>\d+)$', login_required(sedeeact.as_view()), name='sedeeact'),
    url(r'^sedeelim/(?P<pk>\d+)$', login_required(sedeelim.as_view()), name='sedeelim'),
    url(r'^sededeta/(?P<pk>\d+)', login_required(sededeta.as_view()), name='sededeta'),

    url(r'^addciudad', login_required(addciudad.as_view()), name='addciudad'),
    url(r'^ciudadlist', login_required(ciudadlist.as_view()), name='ciudadlist'),
    url(r'^ciudadeact/(?P<pk>\d+)$', login_required(ciudadeact.as_view()), name='ciudadeact'),
    url(r'^ciudadelim/(?P<pk>\d+)$', login_required(ciudadelim.as_view()), name='ciudadelim'),
    url(r'^ciudaddeta/(?P<pk>\d+)', login_required(ciudaddeta.as_view()), name='ciudaddeta'),

    url(r'^addplataforma', login_required(addplataforma.as_view()), name='addplataforma'),
    url(r'^plataforlist', login_required(plataforlist.as_view()), name='plataforlist'),
    url(r'^plataforeact/(?P<pk>\d+)$', login_required(plataforeact.as_view()), name='plataforeact'),
    url(r'^plataforelim/(?P<pk>\d+)$', login_required(plataforelim.as_view()), name='plataforelim'),
    url(r'^platafordeta/(?P<pk>\d+)', login_required(platafordeta.as_view()), name='platafordeta'),

    url(r'^addcontrato', login_required(addcontrato.as_view()), name='addcontrato'),
    url(r'^contratolist', login_required(contratolist.as_view()), name='contratolist'),
    url(r'^contratoeact/(?P<pk>\d+)$', login_required(contratoeact.as_view()), name='contratoeact'),
    url(r'^contratoelim/(?P<pk>\d+)$', login_required(contratoelim.as_view()), name='contratoelim'),
    url(r'^contratodeta/(?P<pk>\d+)', login_required(contratodeta.as_view()), name='contratodeta'),

    url(r'^liexaddcliente', login_required(addclienteliex.as_view()), name='liexaddcliente'),
    url(r'^clienteliexlist', login_required(clienteliexlist.as_view()), name='clienteliexlist'),
    url(r'^clienteliexeact/(?P<pk>\d+)$', login_required(clienteliexeact.as_view()), name='clienteliexeact'),
    url(r'^clienteliexelim/(?P<pk>\d+)$', login_required(clienteliexelim.as_view()), name='clienteliexelim'),
    url(r'^clienteliexdeta/(?P<pk>\d+)', login_required(clienteliexdeta.as_view()), name='clienteliexdeta'),

    url(r'^addcodsalida', login_required(addcodsalida.as_view()), name='addcodsalida'),
    url(r'^codsalidalist', login_required(codsalidalist.as_view()), name='codsalidalist'),
    url(r'^codsalidaeact/(?P<pk>\d+)$', login_required(codsalidaeact.as_view()), name='codsalidaeact'),
    url(r'^codsalidaelim/(?P<pk>\d+)$', login_required(codsalidaelim.as_view()), name='codsalidaelim'),
    url(r'^codsalidadeta/(?P<pk>\d+)', login_required(codsalidadeta.as_view()), name='codsalidadeta'),

    url(r'^addpresalida', login_required(addpresalida.as_view()), name='addpresalida'),
    url(r'^presalidalist', login_required(presalidalist.as_view()), name='presalidalist'),
    url(r'^presalidaeact/(?P<pk>\d+)$', login_required(presalidaeact.as_view()), name='presalidaeact'),
    url(r'^presalidaelim/(?P<pk>\d+)$', login_required(presalidaelim.as_view()), name='presalidaelim'),
    url(r'^presalidadeta/(?P<pk>\d+)', login_required(presalidadeta.as_view()), name='presalidadeta'),

    url(r'^close', login_required(close.as_view()), name='close'),

     )