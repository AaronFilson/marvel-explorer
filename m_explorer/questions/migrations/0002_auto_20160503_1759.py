# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='abilities',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='character',
            name='aliases',
            field=models.CharField(blank=True, max_length=550),
        ),
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='character',
            name='group_aff',
            field=models.CharField(blank=True, max_length=550),
        ),
        migrations.AlterField(
            model_name='character',
            name='origin',
            field=models.CharField(blank=True, max_length=550),
        ),
        migrations.AlterField(
            model_name='character',
            name='paraphernalia',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='character',
            name='powers',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='character',
            name='weapons',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]