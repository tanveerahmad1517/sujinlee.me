# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 06:48
from __future__ import unicode_literals

from django.db import migrations, models
import simplemde.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20170224_1059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=simplemde.fields.SimpleMDEField(verbose_name='mardown content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
    ]
