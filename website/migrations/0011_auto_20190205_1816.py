# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-05 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_donation_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='transaction_id',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]