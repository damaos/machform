from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import plataform, city, seat, contract, typetrunk, trunk, codexit, preexit, client, dnis, linext, enlace, trunkenlace


class plataformform(ModelForm):
    
    class Meta:
        model = plataform
        exclude = ['created_at', 'created_by', 'updated_at', 'updated_by','deleted','ip_forwarded']
        
class clientform(ModelForm):
    
    class Meta:
        model = client
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'deleted','ip_forwarded']
        

class cityform(ModelForm):
    
    class Meta:
        model = city
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'deleted','ip_forwarded']


class seatform(ModelForm):
    
    class Meta:
        model = seat
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'deleted','ip_forwarded']


class contractform(ModelForm):
    
    class Meta:
        model = contract
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'deleted','ip_forwarded']

class typetrunkform(ModelForm):
    
    class Meta:
        model = typetrunk
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'deleted','ip_forwarded']


class trunkform(ModelForm):
    
    class Meta:
        model = trunk
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'deleted','ip_forwarded']

class codexitform(ModelForm):
    
    class Meta:
        model = codexit
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'deleted','ip_forwarded']

class preexitform(ModelForm):
    
    class Meta:
        model = preexit
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'deleted','ip_forwarded']


class dnisform(ModelForm):
    
    class Meta:
        model = dnis
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'deleted','ip_forwarded']


class linextform(ModelForm):
    
    class Meta:
        model = linext
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'deleted','ip_forwarded']

class enlaceform(ModelForm):
    
    class Meta:
        model = enlace
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'deleted','ip_forwarded']

class trunkenlaceform(ModelForm):
    
    class Meta:
        model = trunkenlace
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'deleted','ip_forwarded']

class usuarioform(UserCreationForm):
    class Meta:
        model = User
        fields = [
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'is_superuser',
                    'is_active',
                    'is_staff'
                    ]

        labels = {
                    'username':'Usuario',
                    'first_name':'Nombre',
                    'last_name':'Apellido',
                    'email':'Correo',
                    'is_superuser':'Super usuario',
                    'is_active': 'Activar',
                    'is_staff':'Staff'
                }

