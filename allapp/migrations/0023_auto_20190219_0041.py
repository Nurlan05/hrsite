# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-18 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0022_auto_20190219_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvsend',
            name='apply_for',
            field=models.CharField(blank=True, max_length=1500, null=True, verbose_name='Job'),
        ),
    ]
