# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_auto_20150422_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='date_created',
        ),
    ]
