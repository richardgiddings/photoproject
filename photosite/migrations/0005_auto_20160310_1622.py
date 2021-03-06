# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 16:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photosite', '0004_auto_20160309_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Date category added'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_title',
            field=models.CharField(help_text=b'Enter the title of the photo.', max_length=30),
        ),
    ]
