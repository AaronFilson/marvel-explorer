# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_comics', '0002_auto_20160505_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='title',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
    ]
