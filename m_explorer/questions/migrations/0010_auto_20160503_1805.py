# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_auto_20160503_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='eyes',
            field=models.CharField(blank=True, max_length=6000),
        ),
        migrations.AlterField(
            model_name='character',
            name='first_appearance',
            field=models.CharField(blank=True, max_length=6000),
        ),
        migrations.AlterField(
            model_name='character',
            name='hair',
            field=models.CharField(blank=True, max_length=6000),
        ),
        migrations.AlterField(
            model_name='character',
            name='height',
            field=models.CharField(blank=True, max_length=6000),
        ),
        migrations.AlterField(
            model_name='character',
            name='identity_status',
            field=models.CharField(blank=True, max_length=6000),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(blank=True, max_length=6000),
        ),
        migrations.AlterField(
            model_name='character',
            name='pob',
            field=models.CharField(blank=True, max_length=6000),
        ),
        migrations.AlterField(
            model_name='character',
            name='weight',
            field=models.CharField(blank=True, max_length=6000),
        ),
    ]