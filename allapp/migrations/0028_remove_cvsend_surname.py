# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-07-22 16:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0027_job_draft'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvsend',
            name='surname',
        ),
    ]