# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-27 12:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='birdDate',
        ),
        migrations.RemoveField(
            model_name='people',
            name='departament',
        ),
        migrations.RemoveField(
            model_name='people',
            name='email',
        ),
        migrations.RemoveField(
            model_name='people',
            name='photo',
        ),
        migrations.DeleteModel(
            name='Departament',
        ),
    ]
