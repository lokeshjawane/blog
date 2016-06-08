# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20160606_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloger',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('image', models.FileField(upload_to=blog.models.user_directory_path, default='uploaded_img/img.jpeg')),
                ('user_id', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
