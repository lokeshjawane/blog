# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160606_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloger',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Bloger',
        ),
    ]
