# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_experience_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='content',
            field=models.TextField(max_length=3000),
        ),
    ]
