# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160606_0918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloger',
            old_name='image',
            new_name='img',
        ),
    ]
