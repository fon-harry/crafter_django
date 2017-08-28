# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_mpcost'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='successRate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='type',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
    ]
