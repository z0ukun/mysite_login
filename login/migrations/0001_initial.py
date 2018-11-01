# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('sex', models.CharField(default=b'\xe7\x94\xb7', max_length=32, choices=[(b'male', b'\xe7\x94\xb7'), (b'female', b'\xe5\xa5\xb3')])),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['c_time'],
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
    ]
