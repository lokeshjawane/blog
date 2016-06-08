# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160527_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloger',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user_id', models.IntegerField()),
                ('designation', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('image', models.FileField(default='uploaded_img/img.jpeg', upload_to=blog.models.user_directory_path)),
            ],
        ),
        migrations.DeleteModel(
            name='editor',
        ),
    ]
