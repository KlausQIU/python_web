# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-29 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160628_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='content',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skillname',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='phonenumber',
            field=models.CharField(max_length=100),
        ),
    ]