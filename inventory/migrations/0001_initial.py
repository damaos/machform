# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 13:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima de modificación')),
                ('ip_forwarded', models.CharField(max_length=50, verbose_name='Ip de modificación')),
                ('name_city', models.CharField(max_length=50, verbose_name='Nombre Ciudad ')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_city_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_city_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ultima modificación por')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima de modificación')),
                ('ip_forwarded', models.CharField(max_length=50, verbose_name='Ip de modificación')),
                ('nom_client', models.CharField(max_length=50, verbose_name='Nombre cliente ')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_client_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_client_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ultima modificación por')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='codexit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima de modificación')),
                ('ip_forwarded', models.CharField(max_length=50, verbose_name='Ip de modificación')),
                ('num_code', models.IntegerField(verbose_name='Código de salida ')),
                ('obser_codexit', models.TextField(blank=True, max_length=100, verbose_name='Observación ')),
                ('code_clie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.client', verbose_name='Nombre cliente ')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_codexit_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_codexit_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ultima modificación por')),
            ],
            options={
                'verbose_name': 'Código de salida',
                'verbose_name_plural': 'Códigos de salida',
            },
        ),
        migrations.CreateModel(
            name='contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima de modificación')),
                ('ip_forwarded', models.CharField(max_length=50, verbose_name='Ip de modificación')),
                ('num_contract', models.IntegerField(verbose_name='Número contrato ')),
                ('name_contract', models.CharField(max_length=50, verbose_name='Nombre contrato ')),
                ('obser_contract', models.TextField(blank=True, max_length=100, verbose_name='Observación ')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_contract_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_contract_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ultima modificación por')),
            ],
            options={
                'verbose_name': 'Contrato',
                'verbose_name_plural': 'Contratos',
            },
        ),
        migrations.CreateModel(
            name='dnis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima de modificación')),
                ('ip_forwarded', models.CharField(max_length=50, verbose_name='Ip de modificación')),
                ('num_dnis', models.BigIntegerField(verbose_name='DNIS ')),
                ('num_des', models.IntegerField(verbose_name='Número de desborde ')),
                ('obser_dnis', models.TextField(blank=True, max_length=100, verbose_name='Observación ')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_dnis_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('nom_clie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.client', verbose_name='Cliente ')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_dnis_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ultima modificación por')),
            ],
            options={
                'verbose_name': 'DNIS',
                'verbose_name_plural': 'DNIS',
            },
        ),
        migrations.CreateModel(
            name='enlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima de modificación')),
                ('ip_forwarded', models.CharField(max_length=50, verbose_name='Ip de modificación')),
                ('enla_num', models.BigIntegerField(verbose_name='Número de linea ')),
                ('enla_pro', models.CharField(choices=[('Emtelco', 'Emtelco'), ('Cliente', 'Cliente')], max_length=50, verbose_name='Propietario linea')),
                ('enla_proex', models.CharField(choices=[('Emtelco', 'Emtelco'), ('Cliente', 'Cliente')], max_length=50, verbose_name='Propietario linea externa')),
                ('enla_tartel', models.CharField(max_length=50, verbose_name='Tarjeta telefonica ')),
                ('enla_prov', models.CharField(blank=True, max_length=50, verbose_name='Ubicación proveedor ')),
                ('enla_emt', models.CharField(max_length=50, verbose_name='Ubicación Emtelco ')),
                ('enla_obser', models.TextField(blank=True, max_length=100, verbose_name='Observación ')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_enlace_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('enla_clien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.client', verbose_name='Cliente ')),
            ],
            options={
                'verbose_name': 'Lineas',
                'ordering': ['enla_num'],
                'verbose_name_plural': 'Linea',
            },
        ),
        migrations.CreateModel(
            name='linext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima de modificación')),
                ('ip_forwarded', models.CharField(max_length=50, verbose_name='Ip de modificación')),
                ('num_linext', models.BigIntegerField(verbose_name='Linea externa ')),
                ('obser_linext', models.TextField(blank=True, max_length=100, verbose_name='Observación ')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_linext_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('nom_clie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.client', verbose_name='Cliente ')),
                ('num_prefx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.contract', verbose_name='Número de contrato ')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_linext_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ultima modificación por')),
            ],
            options={
                'verbose_name': 'Linea externa',
                'verbose_name_plural': 'Lineas externas',
            },
        ),
        migrations.CreateModel(
            name='plataform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima de modificación')),
                ('ip_forwarded', models.CharField(max_length=50, verbose_name='Ip de modificación')),
                ('name_plataform', models.CharField(max_length=50, verbose_name='Nombre Plataforma ')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_plataform_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_plataform_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ultima modificación por')),
            ],
            options={
                'verbose_name': 'Plataforma',
                'verbose_name_plural': 'Plataformas',
            },
        ),
        migrations.CreateModel(
            name='preexit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima de modificación')),
                ('ip_forwarded', models.CharField(max_length=50, verbose_name='Ip de modificación')),
                ('num_pref', models.IntegerField(verbose_name='Prefijo de salida ')),
                ('obser_preexit', models.TextField(blank=True, max_length=100, verbose_name='Observación ')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_preexit_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('pref_clie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.client', verbose_name='Nombre cliente ')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_preexit_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ultima modificación por')),
            ],
            options={
                'verbose_name': 'Prefijo de salida',
                'verbose_name_plural': 'Prefijos de salida',
            },
        ),
        migrations.CreateModel(
            name='seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima de modificación')),
                ('ip_forwarded', models.CharField(max_length=50, verbose_name='Ip de modificación')),
                ('name_seat', models.CharField(max_length=50, verbose_name='Nombre Sede ')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_seat_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('name_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.city', verbose_name='Ciudad ')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_seat_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ultima modificación por')),
            ],
            options={
                'verbose_name': 'Sede',
                'verbose_name_plural': 'Sedes',
            },
        ),
        migrations.CreateModel(
            name='trunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima de modificación')),
                ('ip_forwarded', models.CharField(max_length=50, verbose_name='Ip de modificación')),
                ('num_trunk', models.IntegerField(verbose_name='Número troncal ')),
                ('obser_contract', models.TextField(blank=True, max_length=100, verbose_name='Observación ')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_trunk_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
            ],
            options={
                'verbose_name': 'Troncal',
                'ordering': ['num_trunk'],
                'verbose_name_plural': 'Troncales',
            },
        ),
        migrations.CreateModel(
            name='trunkenlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima de modificación')),
                ('ip_forwarded', models.CharField(max_length=50, verbose_name='Ip de modificación')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_trunkenlace_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('num_dnenla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.dnis', verbose_name='DNIS ')),
                ('num_dnlin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.linext', verbose_name='Linea externa ')),
                ('num_enlatr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.enlace', verbose_name='Número de linea ')),
                ('num_trunke', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.trunk', verbose_name='Número troncal ')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_trunkenlace_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ultima modificación por')),
            ],
            options={
                'verbose_name': 'Enlace',
                'ordering': ['num_trunke'],
                'verbose_name_plural': 'Enlaces',
            },
        ),
        migrations.CreateModel(
            name='typetrunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima de modificación')),
                ('ip_forwarded', models.CharField(max_length=50, verbose_name='Ip de modificación')),
                ('type_trunk', models.CharField(max_length=50, verbose_name='Tipo Troncal ')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_typetrunk_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_typetrunk_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ultima modificación por')),
            ],
            options={
                'verbose_name': 'Tipo de troncal',
                'verbose_name_plural': 'Tipos de troncales',
            },
        ),
        migrations.AddField(
            model_name='trunk',
            name='type_trun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.typetrunk', verbose_name='Tipo de troncal '),
        ),
        migrations.AddField(
            model_name='trunk',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_trunk_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ultima modificación por'),
        ),
        migrations.AddField(
            model_name='enlace',
            name='enla_plat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.plataform', verbose_name='Plataforma '),
        ),
        migrations.AddField(
            model_name='enlace',
            name='enla_sed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.seat', verbose_name='Sede '),
        ),
        migrations.AddField(
            model_name='enlace',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_enlace_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ultima modificación por'),
        ),
    ]
