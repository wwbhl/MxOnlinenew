# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-31 21:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180829_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='fav_num',
            new_name='fav_nums',
        ),
    ]
