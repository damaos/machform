from django.contrib import admin
from .models import plataform, city, seat, contract, typetrunk, trunk, codexit, preexit, dnis, linext, client, enlace, trunkenlace
from .forms import plataformform, cityform, seatform, contractform, typetrunkform, trunkform, codexitform, preexitform, clientform, dnisform, linextform, enlaceform,  trunkenlaceform


class plataformadmin(admin.ModelAdmin):

    form = plataformform
    list_display = ('name_plataform', 'created_at', 'created_by', 'updated_at', 'updated_by','ip_forwarded')
    search_fields = ['name_plataform']

class clientadmin(admin.ModelAdmin):
    
    form = clientform
    list_display = ('nom_client', 'created_at', 'created_by', 'updated_at', 'updated_by','ip_forwarded')
    search_fields = ['nom_client']

class cityadmin(admin.ModelAdmin):

    form = cityform
    list_display = ('name_city', 'created_at', 'created_by', 'updated_at', 'updated_by','ip_forwarded')
    search_fields = ['name_city']


class seatadmin(admin.ModelAdmin):
    
    form = seatform
    list_display = ('name_seat', 'name_city', 'created_at', 'created_by', 'updated_at', 'updated_by','ip_forwarded')
    list_filter = ('name_seat', 'name_city')
    search_fields = ['name_seat', 'name_city__name_city']


class contractadmin(admin.ModelAdmin):
    
    form = contractform
    list_display = ('num_contract', 'name_contract', 'obser_contract', 'created_at', 'created_by', 'updated_at', 'updated_by','ip_forwarded')
    search_fields = ['num_contract','name_contract']

class typetrunkadmin(admin.ModelAdmin):

    form = typetrunkform
    list_display = ('type_trunk', 'created_at', 'created_by', 'updated_at', 'updated_by','ip_forwarded')
    search_fields = ['type_trunk']

class codexitadmin(admin.ModelAdmin):
    
    form = codexitform
    list_display = ('num_code', 'code_clie','core', 'obser_codexit', 'created_at', 'created_by', 'updated_at', 'updated_by','ip_forwarded')
    search_fields = ['num_code','code_clie__nom_client']


class preexitadmin(admin.ModelAdmin):
    
    form = preexitform
    list_display = ('num_pref', 'pref_clie', 'obser_preexit', 'created_at', 'created_by', 'updated_at', 'updated_by','ip_forwarded')
    search_fields = ['num_pref', 'pref_clie__nom_client']

class linextadmin(admin.ModelAdmin):

    form = linextform    
    search_fields = ['num_linext']

class dnisadmin(admin.ModelAdmin):

    form = dnisform
    list_display = ('num_dnis', 'nom_clie', 'num_des','obser_dnis','created_at', 'created_by', 'updated_at', 'updated_by','ip_forwarded')
    search_fields = ['num_dnis',  'num_des', 'nom_clie__nom_client']


class enlaceadmin(admin.ModelAdmin):
    
    form = enlaceform
    list_display = ('enla_num','enla_clien','enla_plat')
    search_fields = ['enla_num','enla_tartel','enla_prov','enla_emt','enla_clien__nom_client','enla_sed__name_seat','enla_plat__name_plataform','enla_dns__num_dnis']

class trunkadmin(admin.ModelAdmin):

    form = trunkform
    list_display = ('num_trunk', 'type_trun', 'obser_contract')
    search_fields = ['num_trunk', 'type_trun__type_trunk']

class trunkenlaceadmin(admin.ModelAdmin):

    form = trunkform
    list_display = ('num_trunke', 'num_enlatr', 'num_dnenla', 'num_dnlin')



# Register your models here.
admin.site.register(plataform, plataformadmin)
admin.site.register(city, cityadmin)
admin.site.register(seat, seatadmin)
admin.site.register(contract, contractadmin)
admin.site.register(typetrunk, typetrunkadmin)
admin.site.register(trunk, trunkadmin)
admin.site.register(codexit, codexitadmin)
admin.site.register(preexit, preexitadmin)  #Prefijo de salida
admin.site.register(dnis, dnisadmin)
admin.site.register(linext, linextadmin)
admin.site.register(client, clientadmin)
admin.site.register(enlace, enlaceadmin)
admin.site.register(trunkenlace, trunkenlaceadmin)



