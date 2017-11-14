# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 00:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0004_pessoa_chefe'),
    ]

    operations = [
        migrations.AddField(
            model_name='frequencia',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ponto.TipoRegistro'),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='status',
            field=models.CharField(choices=[('valido', 'Consitente'), ('ivalido', 'Inconsistente')], default='Consistente', max_length=20),
        ),
    ]
