# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_created',
            field=models.DateTimeField(default=b'', verbose_name=b'date created', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='rack',
            field=models.ForeignKey(to='parking.Rack'),
        ),
    ]
