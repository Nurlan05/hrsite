# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-18 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0012_auto_20190218_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_location',
            field=models.ManyToManyField(related_name='location', to='allapp.Location', verbose_name='Job location'),
        ),
    ]
