# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-04-13 06:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_services', '0010_auto_20180413_0656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layer',
            name='time_mosaic_date_regex',
        ),
        migrations.RemoveField(
            model_name='layer',
            name='time_mosaic_elev_regex',
        ),
        migrations.RemoveField(
            model_name='layer',
            name='time_resolution',
        ),        
    ]
