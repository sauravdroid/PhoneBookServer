# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-04 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_no',
            field=models.CharField(default='N/A', max_length=15),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone_no',
            field=models.CharField(default='N/A', max_length=15),
        ),
    ]
