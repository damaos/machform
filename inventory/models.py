from django.db import models
from src.model import BaseModel
from django.utils import timezone
from django.contrib.auth.models import Group

#Plataforma
class plataform(BaseModel):
    name_plataform = models.CharField('Nombre Plataforma ', max_length=50, unique=True )

    def __str__(self):
    	return '%s' % (self.name_plataform)

    class Meta:
    	verbose_name_plural = 'Plataformas'
    	verbose_name = 'Plataforma'

#Clientes
class client(BaseModel):
    nom_client = models.CharField('Nombre cliente ',max_length=50, unique=True  )
      

    def __str__(self):
        return '%s' % (self.nom_client)

    class Meta:
        verbose_name_plural = 'Clientes'
        verbose_name = 'Cliente'

#Ciudad
class city(BaseModel):
    name_city = models.CharField('Nombre Ciudad ', max_length=50, unique=True)

    def __str__(self):
    	return '%s' % (self.name_city)

    class Meta:
    	verbose_name_plural = 'Ciudades'
    	verbose_name = 'Ciudad'
#Sede
class seat(BaseModel):
    name_seat = models.CharField('Nombre Sede ', max_length=50, unique=True)
    name_city = models.ForeignKey(city, verbose_name='Ciudad ')

    def __str__(self):
    	return '%s' % (self.name_seat)

    class Meta:
    	verbose_name_plural = 'Sedes'
    	verbose_name = 'Sede'
#Contrato
class contract(BaseModel):
    num_contract = models.CharField('Número contrato ', unique=True, max_length=255 )
    name_contract = models.CharField('Nombre contrato ', max_length=50)
    obser_contract = models.TextField('Observación ', max_length=100,blank=True)
    

    def __str__(self):
    	return '%s' % (self.num_contract)

    class Meta:
    	verbose_name_plural = 'Contratos'
    	verbose_name = 'Contrato'
#Tipo Troncal
class typetrunk(BaseModel):
    type_trunk = models.CharField('Tipo Troncal ', max_length=50, unique=True)
      

    def __str__(self):
    	return '%s' % (self.type_trunk)

    class Meta:
    	verbose_name_plural = 'Tipos de troncales'
    	verbose_name = 'Tipo de troncal'

#Codigo de salida
class codexit(BaseModel):
    CORE = (
            (1,'1'),
            (2,'2'),
            (3,'3'),
            (4,'4')
    )
    num_code = models.IntegerField('Código de salida ', unique=True)
    code_clie = models.ForeignKey(client, verbose_name='Nombre cliente ' )
    core = models.IntegerField('Core', choices=CORE )
    obser_codexit = models.TextField('Observación ', max_length=100,blank=True)
    

    def __str__(self):
    	return '%s' % (self.num_code)

    class Meta:
        verbose_name_plural = 'Códigos de salida'
        verbose_name = 'Código de salida'
        ordering = ['num_code']


#Prefijo de salida
class preexit(BaseModel):
    num_pref = models.IntegerField('Prefijo de salida ', unique=True)
    pref_clie = models.ForeignKey(client, verbose_name='Nombre cliente ')
    obser_preexit = models.TextField('Observación ', max_length=100, blank=True)
    

    def __str__(self):
    	return '%s' % (self.num_pref)

    class Meta:
        ordering = ['num_pref']
        verbose_name_plural = 'Prefijos de salida'
        verbose_name = 'Prefijo de salida'


#Linea externa
class linext(BaseModel):
    num_linext = models.CharField('Linea externa ', unique=True, max_length=255)
    num_prefx = models.ForeignKey(contract, verbose_name='Número de contrato ')  #Numero contrato
    nom_clie = models.ForeignKey(client, verbose_name='Cliente ')
    obser_linext= models.TextField('Observación ', max_length=100, blank=True)
    

    def __str__(self):
        return '%s' % (self.num_linext)

    class Meta:
        verbose_name_plural = 'Lineas externas'
        verbose_name = 'Linea externa'
        ordering = ['num_linext']

#DNIS
class dnis(BaseModel):
    num_dnis = models.CharField('DNIS ', unique=True, max_length=255)
    nom_clie = models.ForeignKey(client, verbose_name='Cliente ')
    num_des = models.CharField('Número de desborde ', blank=True, null=True, max_length=255) #número de desborde
    obser_dnis = models.TextField('Observación ', max_length=100, blank=True)
    

    def __str__(self):
        return '%s' % (self.num_dnis)

    class Meta:
        verbose_name_plural = 'DNIS'
        verbose_name = 'DNIS'
        ordering = ['num_dnis']


#Enlace
class enlace(BaseModel):

    PROPIETARIO = (
            ('Emtelco','Emtelco'),
            ('Cliente','Cliente')
    )
    enla_num = models.CharField('Número de linea ', max_length=50,  unique=True)
    enla_pro = models.CharField('Propietario linea', choices=PROPIETARIO, max_length=50)
    enla_clien = models.ForeignKey(client, verbose_name='Cliente ' ) #Clientes
    enla_sed = models.ForeignKey(seat, verbose_name='Sede ')  #Sede
    enla_plat = models.ForeignKey(plataform, verbose_name='Plataforma ' ) #plataforma
    enla_tartel = models.CharField('Tarjeta telefonica ',max_length=50 )#tarjeta telefonica
    enla_prov = models.CharField('Ubicación proveedor ',max_length=50, blank=True )#Ubicación proveedor
    enla_emt = models.CharField('Ubicación Emtelco ',max_length=50 )#Ubicación emtelco
    enla_obser= models.TextField('Observación ', max_length=100, blank=True)

    def __str__(self):
        return '%s' % (self.enla_num)

    class Meta:
        verbose_name_plural = 'Linea'
        verbose_name = 'Lineas'
        ordering = ['enla_num']

#Troncal
class trunk(BaseModel):
    num_trunk = models.CharField('Número troncal ', unique=True, max_length=250)
    type_trun = models.ForeignKey(typetrunk, verbose_name='Tipo de troncal ')
    #trunk_enla = models.ForeignKey(enlace, verbose_name='Enlace ' ) 
    obser_contract = models.TextField('Observación ', max_length=100, blank=True)
    

    def __str__(self):
        return '%s' % (self.num_trunk)

    class Meta:
        verbose_name_plural = 'Troncales'
        verbose_name = 'Troncal'
        ordering = ['num_trunk']


#enlace troncal-linea-dnis-externa
class trunkenlace(BaseModel):
    num_trunke = models.ForeignKey(trunk, verbose_name='Número troncal ')
    num_enlatr = models.ForeignKey(enlace, verbose_name='Número de linea ' )
    num_dnenla = models.ForeignKey(dnis, verbose_name='DNIS ')
    num_dnlin = models.ForeignKey(linext, verbose_name='Linea externa ' )
    obser = models.TextField('Observación', max_length=100, blank=True )    

    def __str__(self):
        return '%s' % (self.num_trunke)
        
    class Meta:
        verbose_name_plural = 'Enlaces'
        verbose_name = 'Enlace'
        ordering = ['num_trunke']