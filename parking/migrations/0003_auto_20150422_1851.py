# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_auto_20150422_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name=b'date created', null=True),
        ),
    ]
