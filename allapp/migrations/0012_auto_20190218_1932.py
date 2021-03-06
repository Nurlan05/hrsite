# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-18 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0011_auto_20190218_1905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hours',
            options={'verbose_name': 'Hours', 'verbose_name_plural': 'Hours'},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-id'], 'verbose_name': 'Vacancy', 'verbose_name_plural': 'Vacancies'},
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_location',
        ),
        migrations.AddField(
            model_name='job',
            name='job_location',
            field=models.ManyToManyField(null=True, related_name='location', to='allapp.Location', verbose_name='Job location'),
        ),
    ]
