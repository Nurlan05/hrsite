# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-18 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0015_auto_20190218_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvsend',
            name='email',
            field=models.EmailField(max_length=1500, verbose_name='Email'),
        ),
    ]