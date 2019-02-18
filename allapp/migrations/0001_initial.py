# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-18 12:29
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1500, verbose_name='Başlıq')),
                ('title_az', models.CharField(max_length=1500, null=True, verbose_name='Başlıq')),
                ('title_en', models.CharField(max_length=1500, null=True, verbose_name='Başlıq')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Haqqında')),
                ('content_az', ckeditor.fields.RichTextField(null=True, verbose_name='Haqqında')),
                ('content_en', ckeditor.fields.RichTextField(null=True, verbose_name='Haqqında')),
                ('slug', models.SlugField(editable=False, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Vakansiya',
                'verbose_name_plural': 'Vakansiyalar',
            },
        ),
    ]
