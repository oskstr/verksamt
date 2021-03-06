# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-20 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('verksamhetsplan', '0010_auto_20170901_0203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='suggested_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='verksamhetsplan.Status'),
        ),
    ]
