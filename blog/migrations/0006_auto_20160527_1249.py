# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160527_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='editor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('designation', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('image', models.FileField(default=b'uploaded_img/img.jpeg', upload_to=blog.models.user_directory_path)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
