# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-10-08 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('best_deals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='business',
            name='categories',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
