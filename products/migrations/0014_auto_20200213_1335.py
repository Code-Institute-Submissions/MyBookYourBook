# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-13 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20200213_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rentprice_per_week',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='saleprice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
    ]
