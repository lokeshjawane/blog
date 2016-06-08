# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_bloger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloger',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='bloger',
            name='id',
            field=models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
