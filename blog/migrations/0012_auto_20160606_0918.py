# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_auto_20160606_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloger',
            name='user_id',
            field=models.ForeignKey(default='', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bloger',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True),
        ),
    ]
