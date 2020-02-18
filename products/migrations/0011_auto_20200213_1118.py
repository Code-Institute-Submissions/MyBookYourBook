# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-13 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200210_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_for_rent',
            field=models.BooleanField(default=False, verbose_name='For rent?'),
        ),
    ]