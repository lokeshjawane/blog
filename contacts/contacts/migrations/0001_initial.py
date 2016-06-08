# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import contacts.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('mname', models.CharField(default=b'SOME STRING', max_length=20)),
                ('image', models.FileField(upload_to=contacts.models.user_directory_path)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comments',
            name='f_name',
            field=models.ForeignKey(to='contacts.Contacts'),
            preserve_default=True,
        ),
    ]
