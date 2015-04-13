# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.CharField(max_length=50)),
                ('lng', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('capacity', models.IntegerField(max_length=3, null=b'True')),
                ('covered', models.BooleanField(default=False)),
                ('intended', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('lat', 'lng', 'description', 'capacity', 'covered', 'intended'),
                'verbose_name_plural': 'racks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('rating', models.IntegerField(max_length=1, null=b'True')),
                ('review', models.CharField(max_length=1000)),
                ('crime', models.BooleanField(default=False)),
                ('rack', models.ForeignKey(to='parking.rack')),
            ],
            options={
                'ordering': ('username', 'rating', 'review'),
                'verbose_name_plural': 'reviews',
            },
            bases=(models.Model,),
        ),
    ]
