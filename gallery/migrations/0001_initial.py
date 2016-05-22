# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name=b'image')),
                ('name', models.CharField(default=b'', max_length=200, verbose_name=b'Item Name')),
                ('description', models.TextField(default=b'')),
                ('price', models.DecimalField(max_digits=b'6', decimal_places=b'2')),
            ],
        ),
    ]
