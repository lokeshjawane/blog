# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160606_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloger',
            name='img',
            field=models.FileField(upload_to=blog.models.user_directory_path),
        ),
    ]
