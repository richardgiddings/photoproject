# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photosite', '0002_photo_photo_full'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_date',
            field=models.DateTimeField(verbose_name=b'Date category added'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_title',
            field=models.CharField(help_text=b'The name of the category.', max_length=50),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text=b'When was the photo taken?', verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_description',
            field=models.TextField(help_text=b'Enter a description for the photo.', max_length=500),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_full',
            field=models.ImageField(help_text=b'The full size image.', upload_to=b'full'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_title',
            field=models.CharField(help_text=b'Enter the title of the photo.', max_length=50),
        ),
    ]
