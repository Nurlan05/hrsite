# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-18 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(editable=False, unique=True, verbose_name='Slug'),
        ),
    ]
