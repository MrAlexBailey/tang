# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-20 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190120_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='transaction_id',
            field=models.CharField(default='AZD1234', max_length=100),
            preserve_default=False,
        ),
    ]
