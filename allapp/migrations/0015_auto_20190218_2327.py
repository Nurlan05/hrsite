# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-18 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0014_cvsend'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cvsend',
            options={'verbose_name': 'CV', 'verbose_name_plural': 'ALL CV'},
        ),
        migrations.AddField(
            model_name='cvsend',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]