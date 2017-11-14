# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 00:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0002_auto_20171113_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='pessoa',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='horario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ponto.Horario'),
        ),
    ]
