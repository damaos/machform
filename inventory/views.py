from machform import settings
from inventory.forms import *
from django.db.models import Q
from django.db import connection
from django.contrib import messages
from django.shortcuts import render
from .filters import TrunkenlaFilter
from django.views.generic import View
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from .models import plataform, city, seat, contract, typetrunk, trunk, codexit, preexit, dnis, linext, client, enlace,trunkenlace
from .forms import trunkform, enlaceform, dnisform, linextform


class first_view(View):

    template_name = 'index.html'
    @method_decorator(login_required(login_url='/login/logout'))
    def get(self, request, *args, **kwargs):
        request.session.set_expiry(settings.SESSION_TIMEOUT)
        return render(request, self.template_name, {})

class ver_troncales(View):
    template_name = 'vertroncales.html'
    @method_decorator(login_required(login_url='/login/logout'))
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        if q:
            request.session.set_expiry(settings.SESSION_TIMEOUT)            
            #trunklis = trunkenlace.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin").filter(Q(num_trunke__num_trunk__icontains=q)| Q(num_trunke__type_trun__type_trunk__icontains=q)| Q(num_enlatr__enla_num__icontains=q)| Q(num_dnenla__num_dnis__icontains=q)| Q(num_dnlin__num_linext__icontains=q))
            trunklis = trunkenlace.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin").filter(Q(num_trunke__num_trunk__icontains=q))

            return render(request, self.template_name, {'trunklis':trunklis})
        else:
            request.session.set_expiry(settings.SESSION_TIMEOUT)
            trunklis = trunkenlace.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin")
            return render(request, self.template_name, {'trunklis':trunklis})

class trunkenlacelist(ListView):
    model = trunkenlace
    #template_name = 'trunkenlace_list.html'
    paginate_by = 20

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        p = self.request.GET.get('p', '')
        r = self.request.GET.get('r', '')
        s = self.request.GET.get('s', '')
        
        
        if q != "":
            
            self.request.session.set_expiry(settings.SESSION_TIMEOUT)            
            #object_list = self.model.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin").filter(Q(num_trunke__num_trunk__icontains=q)| Q(num_trunke__type_trun__type_trunk__icontains=q)| Q(num_enlatr__enla_num__icontains=q)| Q(num_dnenla__num_dnis__icontains=q)| Q(num_dnlin__num_linext__icontains=q))
            object_list = trunkenlace.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin").filter(Q(num_trunke__num_trunk__icontains=q)| Q(num_trunke__type_trun__type_trunk__icontains=q))

            return object_list
        # else:
        #     self.request.session.set_expiry(settings.SESSION_TIMEOUT)
        #     object_list = self.model.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin")
        #     return object_list
        if p != "":
            
            self.request.session.set_expiry(settings.SESSION_TIMEOUT)            
            #object_list = self.model.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin").filter(Q(num_trunke__num_trunk__icontains=q)| Q(num_trunke__type_trun__type_trunk__icontains=q)| Q(num_enlatr__enla_num__icontains=q)| Q(num_dnenla__num_dnis__icontains=q)| Q(num_dnlin__num_linext__icontains=q))
            object_list = trunkenlace.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin").filter(Q(num_enlatr__enla_num__icontains=p))

            return object_list

        if r != "":
            
            self.request.session.set_expiry(settings.SESSION_TIMEOUT)            
            #object_list = self.model.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin").filter(Q(num_trunke__num_trunk__icontains=q)| Q(num_trunke__type_trun__type_trunk__icontains=q)| Q(num_enlatr__enla_num__icontains=q)| Q(num_dnenla__num_dnis__icontains=q)| Q(num_dnlin__num_linext__icontains=q))
            object_list = trunkenlace.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin").filter(Q(num_dnenla__num_dnis__icontains=r))

            return object_list
        if s != "":
            
            self.request.session.set_expiry(settings.SESSION_TIMEOUT)            
            #object_list = self.model.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin").filter(Q(num_trunke__num_trunk__icontains=q)| Q(num_trunke__type_trun__type_trunk__icontains=q)| Q(num_enlatr__enla_num__icontains=q)| Q(num_dnenla__num_dnis__icontains=q)| Q(num_dnlin__num_linext__icontains=q))
            object_list = trunkenlace.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin").filter(Q(num_dnlin__num_linext__icontains=s))

            return object_list
        
        else:
            self.request.session.set_expiry(settings.SESSION_TIMEOUT)
            object_list = self.model.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin")
            return object_list


class regis_troncal(CreateView):
    model = trunkenlace
    success_url = reverse_lazy('inventory:trunkenlacelist')
    fields = ['num_trunke', 'num_enlatr', 'num_dnenla','num_dnlin','obser']


class edit_troncal(UpdateView):

    template_name = 'editroncal.html'
    @method_decorator(login_required(login_url='/login/logout'))
    def get(self, request, *args, **kwargs):
        request.session.set_expiry(settings.SESSION_TIMEOUT)

        tron_edit = trunkenlace.objects.get(pk=kwargs['pk'])
        form = trunkenlaceform(instance=tron_edit)
        

        return render(request, self.template_name, {
            'form': form,
        })
    def post(self, request, *args, **kwargs):
        request.session.set_expiry(settings.SESSION_TIMEOUT)

        tron_edit = trunkenlace.objects.get(pk=kwargs['pk'])
        form = trunkenlaceform(request.POST,instance=tron_edit)

        tron_edit = form.save()
        messages.info(request, 'El usuario se ha actualizado exitosamente.')
        return HttpResponseRedirect(reverse('inventory:trunkenlacelist'))
    # model = trunkenlace
    # success_url = reverse_lazy('inventory:trunkenlacelist')
    # fields = ['num_trunke', 'num_enlatr', 'num_dnenla','num_dnlin','obser']

class elim_troncal(DeleteView):
    model = trunkenlace
    success_url = reverse_lazy('inventory:trunkenlacelist')


class trunk_info(View):

    template_name = 'detalletroncal.html'
    @method_decorator(login_required(login_url='/login/logout'))
    def get(self, request, *args, **kwargs):
        request.session.set_expiry(settings.SESSION_TIMEOUT)
        q = request.GET.get('q', '')
        if q:
            request.session.set_expiry(settings.SESSION_TIMEOUT)            
            trunklis = trunkenlace.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin").filter(Q(id__icontains=q))
            return render(request, self.template_name, {'trunklis':trunklis})
        else:
            request.session.set_expiry(settings.SESSION_TIMEOUT)
            trunklis = trunkenlace.objects.select_related("num_trunke", "num_enlatr","num_dnenla","num_dnlin")
            return render(request, self.template_name, {'trunklis':trunklis})

class trunk_enla(View):
    template_name = 'detalletrunk.html'
    @method_decorator(login_required(login_url='/login/logout'))
    def get(self, request, *args, **kwargs):
        request.session.set_expiry(settings.SESSION_TIMEOUT)
        q = request.GET.get('q', '')
        
        if q:
            request.session.set_expiry(settings.SESSION_TIMEOUT)
            filtro = (Q(num_trunke__id__icontains=q))
            enlalista = trunkenlace.objects.filter(filtro)
            for i in enlalista:
                id = i
            enlalis = enlalista.values("num_enlatr__enla_num","num_enlatr__id").distinct()
            return render(request, self.template_name, {'enlalis':enlalis,
                                                        'id':id})
        else:
            request.session.set_expiry(settings.SESSION_TIMEOUT)
            return render(request, self.template_name, {'enlalis':enlalis})

class enla_dnis(View):
    template_name = 'detallenum.html'
    @method_decorator(login_required(login_url='/login/logout'))
    def get(self, request, *args, **kwargs):
        request.session.set_expiry(settings.SESSION_TIMEOUT)
        q = request.GET.get('q', '')
        if q:
            request.session.set_expiry(settings.SESSION_TIMEOUT)
            filtro = (Q(num_enlatr__id__icontains=q))
            enlalista = trunkenlace.objects.filter(filtro)
            ids = enlalista.values("num_enlatr__enla_num").distinct()
            enlalis = enlalista.values("num_dnenla__num_dnis","num_dnenla__id").distinct()
            return render(request, self.template_name, {'enlalis':enlalis,
                                                        'ids':ids})
        else:
            request.session.set_expiry(settings.SESSION_TIMEOUT)
            return render(request, self.template_name, {'enlalis':enlalis})

class dnis_liext(View):
    template_name = 'detallednis.html'
    @method_decorator(login_required(login_url='/login/logout'))
    def get(self, request, *args, **kwargs):
        request.session.set_expiry(settings.SESSION_TIMEOUT)
        q = request.GET.get('q', '')
        if q:
            request.session.set_expiry(settings.SESSION_TIMEOUT)
            filtro = (Q(num_dnenla__id__icontains=q))
            enlalis = trunkenlace.objects.filter(filtro)
            return render(request, self.template_name, {'enlalis':enlalis})
        else:
            request.session.set_expiry(settings.SESSION_TIMEOUT)
            enlalis = trunkenlace.objects.all()
            return render(request, self.template_name, {'enlalis':enlalis})


#troncales
class addtrunk(CreateView):
    # model = trunk
    # success_url = reverse_lazy('inventory:registroncal')
    # fields = ['num_trunk', 'type_trun', 'obser_contract']

    template_name = 'inventory/trunk_form.html'
    def get(self, request, *args, **kwargs):
        form = trunkform()
        output = {
            'form':form
        }
        return render(request, self.template_name, output)

    def post(self, request):

        form = trunkform(request.POST)
        form_trunk = trunkform()

        if not form.is_valid():
            output = {
            'form': form,
            'error': True,
            }
            return render(request, self.template_name, output)

        troncal = form.save()
        idtroncal = troncal.id
        output = {'idtroncal': idtroncal,
                    'form': form_trunk}
        
        return render(request, self.template_name, output)

class trunkelist(ListView):
    model = trunk
    paginate_by = 15
class trunkeact(UpdateView):
    model = trunk
    success_url = reverse_lazy('inventory:trunkelist')
    fields = ['num_trunk', 'type_trun', 'obser_contract']
class trunkelim(DeleteView):
    model = trunk
    success_url = reverse_lazy('inventory:trunkelist')
class trunkdeta(DetailView):
    model = trunk


#Numero linea

class addlinea(CreateView):
    # model = enlace
    # success_url = reverse_lazy('inventory:registroncal')
    # fields = ['enla_num', 'enla_pro', 'enla_proex', 'enla_clien', 'enla_sed', 'enla_plat', 'enla_tartel', 'enla_prov', 'enla_emt', 'enla_obser']

    template_name = 'inventory/enlace_form.html'
    def get(self, request, *args, **kwargs):
        form = enlaceform()
        output = {
            'form':form
        }
        return render(request, self.template_name, output)

    def post(self, request):

        form = enlaceform(request.POST)
        form_enlace = enlaceform()

        if not form.is_valid():
            output = {
            'form': form,
            'error': True,
            }
            return render(request, self.template_name, output)

        enlace = form.save()
        idenlace = enlace.id
        output = {'idenlace': idenlace,
                    'form': form_enlace}
        
        return render(request, self.template_name, output)
class linealist(ListView):
    model = enlace
    paginate_by = 15

class lineaeact(UpdateView):
    model = enlace
    success_url = reverse_lazy('inventory:linealist')
    fields = ['enla_num', 'enla_pro', 'enla_proex', 'enla_clien', 'enla_sed', 'enla_plat', 'enla_tartel', 'enla_prov', 'enla_emt', 'enla_obser']
class lineaelim(DeleteView):
    model = enlace
    success_url = reverse_lazy('inventory:linealist')
class lineadeta(DetailView):
    model = enlace


#DNIS

class adddnis(CreateView):
    # model = dnis
    # success_url = reverse_lazy('inventory:registroncal')
    # fields = ['num_dnis', 'num_des', 'nom_clie',  'obser_dnis']

    template_name = 'inventory/dnis_form.html'
    def get(self, request, *args, **kwargs):
        form = dnisform()
        output = {
            'form':form
        }
        return render(request, self.template_name, output)

    def post(self, request):

        form = dnisform(request.POST)
        form_dnis = dnisform()

        if not form.is_valid():
            output = {
            'form': form,
            'error': True,
            }
            return render(request, self.template_name, output)

        dnis = form.save()
        iddnis = dnis.id
        output = {'iddnis': iddnis,
                    'form': form_dnis}
        
        return render(request, self.template_name, output)
class dnislist(ListView):
    model = dnis
    paginate_by = 15
class dniseact(UpdateView):
    model = dnis
    success_url = reverse_lazy('inventory:dnislist')
    fields = ['num_dnis', 'num_des', 'nom_clie',  'obser_dnis']
class dniselim(DeleteView):
    model = dnis
    success_url = reverse_lazy('inventory:dnislist')
class dnisdeta(DetailView):
    model = dnis


#Linea externa

class addliext(CreateView):
    # model = linext
    # success_url = reverse_lazy('inventory:registroncal')
    # fields = ['num_linext', 'num_prefx', 'nom_clie',  'obser_linext']

    template_name = 'inventory/linext_form.html'
    def get(self, request, *args, **kwargs):
        form = linextform()
        output = {
            'form':form
        }
        return render(request, self.template_name, output)

    def post(self, request):

        form = linextform(request.POST)
        form_linext = linextform()

        if not form.is_valid():
            output = {
            'form': form,
            'error': True,
            }
            return render(request, self.template_name, output)

        linext = form.save()
        idlinext = linext.id
        output = {'idlinext': idlinext,
                    'form': form_linext}
        
        return render(request, self.template_name, output)


class linextlist(ListView):
    model = linext
    paginate_by = 20
class linexteact(UpdateView):
    model = linext
    success_url = reverse_lazy('inventory:linextlist')
    fields = ['num_linext', 'num_prefx', 'nom_clie',  'obser_linext']
class linextelim(DeleteView):
    model = linext
    success_url = reverse_lazy('inventory:linextlist')
class linextdeta(DetailView):
    model = linext


#Tipo troncal
class addtiptrunk(CreateView):
    model = typetrunk
    success_url = reverse_lazy('inventory:addtroncal')
    fields = ['type_trunk']
class tiptrunklist(ListView):
    model = typetrunk
    paginate_by = 15
class tiptrunkeact(UpdateView):
    model = typetrunk
    success_url = reverse_lazy('inventory:tiptrunklist')
    fields = ['type_trunk']
class tiptrunkelim(DeleteView):
    model = typetrunk
    success_url = reverse_lazy('inventory:tiptrunklist')
class tiptrunkdeta(DetailView):
    model = typetrunk



#Cliente

class addcliente(CreateView):
    model = client
    success_url = reverse_lazy('inventory:close')
    fields = ['nom_client']


class clienlist(ListView):
    model = client
    paginate_by = 15
class clieneact(UpdateView):
    model = client
    success_url = reverse_lazy('inventory:clienlist')
    fields = ['nom_client']
class clienelim(DeleteView):
    model = client
    success_url = reverse_lazy('inventory:clienlist')
class cliendeta(DetailView):
    model = client




#Sede

class addsede(CreateView):
    model = seat
    success_url = reverse_lazy('inventory:addlinea')
    fields = ['name_seat','name_city']

class sedelist(ListView):
    model = seat
    paginate_by = 15
class sedeeact(UpdateView):
    model = seat
    success_url = reverse_lazy('inventory:sedelist')
    fields = ['name_seat','name_city']
class sedeelim(DeleteView):
    model = seat
    success_url = reverse_lazy('inventory:sedelist')
class sededeta(DetailView):
    model = seat


#Ciudad

class addciudad(CreateView):
    model = city
    success_url = reverse_lazy('inventory:addsede')
    fields = ['name_city']

class ciudadlist(ListView):
    model = city
    paginate_by = 15
class ciudadeact(UpdateView):
    model = city
    success_url = reverse_lazy('inventory:ciudadlist')
    fields = ['name_city','name_city']
class ciudadelim(DeleteView):
    model = city
    success_url = reverse_lazy('inventory:ciudadlist')
class ciudaddeta(DetailView):
    model = city

#Plataforma

class addplataforma(CreateView):
    model = plataform
    success_url = reverse_lazy('inventory:addlinea')
    fields = ['name_plataform']

class plataforlist(ListView):
    model = plataform
    paginate_by = 15
class plataforeact(UpdateView):
    model = plataform
    success_url = reverse_lazy('inventory:plataforlist')
    fields = ['name_plataform']
class plataforelim(DeleteView):
    model = plataform
    success_url = reverse_lazy('inventory:plataforlist')
class platafordeta(DetailView):
    model = plataform





class addclientednis(CreateView):
    model = client
    success_url = reverse_lazy('inventory:close')
    fields = ['nom_client']




#Cliente linea externa
class addclienteliex(CreateView):
    model = client
    success_url = reverse_lazy('inventory:close')
    fields = ['nom_client']

class clienteliexlist(ListView):
    model = client
    paginate_by = 15
class clienteliexeact(UpdateView):
    model = client
    success_url = reverse_lazy('inventory:clienteliexlist')
    fields = ['nom_client']
class clienteliexelim(DeleteView):
    model = client
    success_url = reverse_lazy('inventory:clienteliexlist')
class clienteliexdeta(DetailView):
    model = client




#Contrato
class addcontrato(CreateView):
    model = contract
    success_url = reverse_lazy('inventory:addliext')
    fields = ['num_contract','name_contract','obser_contract']

class contratolist(ListView):
    model = contract
    paginate_by = 15
class contratoeact(UpdateView):
    model = contract
    success_url = reverse_lazy('inventory:contratolist')
    fields = ['num_contract','name_contract','obser_contract']
class contratoelim(DeleteView):
    model = contract
    success_url = reverse_lazy('inventory:contratolist')
class contratodeta(DetailView):
    model = contract

#Usuarios

class addusuario(CreateView):
    model = User
    form_class = usuarioform
    success_url = reverse_lazy('inventory:usuariolist')

class usuariolist(ListView):
    model = User
    paginate_by = 15

class usuarioeact(UpdateView):
    model = User
    success_url = reverse_lazy('inventory:usuariolist')
    fields = ['username','first_name','last_name','email','is_superuser','is_active', 'is_staff']

class usuarioelim(DeleteView):
    model = User
    success_url = reverse_lazy('inventory:usuariolist')


class close(View):
    template_name = 'close.html'
    @method_decorator(login_required(login_url='/login/logout'))
    def get(self, request, *args, **kwargs):
        request.session.set_expiry(settings.SESSION_TIMEOUT)
        return render(request, self.template_name, {})


#Codigos de salida
class addcodsalida(CreateView):
    model = codexit
    success_url = reverse_lazy('inventory:codsalidalist')
    fields = ['num_code','core','code_clie','obser_codexit']

class codsalidalist(ListView):
    model = codexit
    paginate_by = 15

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        if q:
            
            self.request.session.set_expiry(settings.SESSION_TIMEOUT)
            object_list = codexit.objects.filter(Q(num_code__icontains=q) | Q(code_clie__nom_client__icontains=q))

            return object_list
        
        else:
            self.request.session.set_expiry(settings.SESSION_TIMEOUT)
            object_list = self.model.objects.all()
            return object_list

class codsalidaeact(UpdateView):
    model = codexit
    success_url = reverse_lazy('inventory:codsalidalist')
    fields = ['num_code','core','code_clie','obser_codexit']
class codsalidaelim(DeleteView):
    model = codexit
    success_url = reverse_lazy('inventory:codsalidalist')
class codsalidadeta(DetailView):
    model = codexit


#Prefijo de salida
class addpresalida(CreateView):
    model = preexit
    success_url = reverse_lazy('inventory:presalidalist')
    fields = ['num_pref','pref_clie','obser_preexit']

class presalidalist(ListView):
    model = preexit
    paginate_by = 15
    def get_queryset(self):
        q = self.request.GET.get('q', '')
        if q:
            
            self.request.session.set_expiry(settings.SESSION_TIMEOUT)
            object_list = preexit.objects.filter(Q(num_pref__icontains=q) | Q(pref_clie__nom_client__icontains=q))

            return object_list
        
        else:
            self.request.session.set_expiry(settings.SESSION_TIMEOUT)
            object_list = self.model.objects.all()
            return object_list
class presalidaeact(UpdateView):
    model = preexit
    success_url = reverse_lazy('inventory:presalidalist')
    fields = ['num_pref','pref_clie','obser_preexit']
class presalidaelim(DeleteView):
    model = preexit
    success_url = reverse_lazy('inventory:presalidalist')
class presalidadeta(DetailView):
    model = preexit