# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-20 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_donation_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='address',
            field=models.TextField(default='1 Lone Street, Texas, 30131'),
            preserve_default=False,
        ),
    ]
