# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160511121919 on 2016-05-27 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentee',
            field=models.CharField(default='', max_length=100),
        ),
    ]