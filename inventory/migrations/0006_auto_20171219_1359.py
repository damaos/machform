# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-19 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20171130_1048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='codexit',
            options={'ordering': ['num_code'], 'verbose_name': 'Código de salida', 'verbose_name_plural': 'Códigos de salida'},
        ),
        migrations.AlterModelOptions(
            name='linext',
            options={'ordering': ['num_linext'], 'verbose_name': 'Linea externa', 'verbose_name_plural': 'Lineas externas'},
        ),
        migrations.AddField(
            model_name='codexit',
            name='core',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=None, verbose_name='Core'),
            preserve_default=False,
        ),
    ]
