# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-04 18:54
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]