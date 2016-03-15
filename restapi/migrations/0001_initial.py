# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(serialize=False, primary_key=True)),
                ('category_name', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'ordering': ('category_id',),
                'db_table': 'category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(serialize=False, primary_key=True)),
                ('task_name', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'ordering': ('task_id',),
                'db_table': 'task',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=255, blank=True)),
                ('email', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'ordering': ('user_id',),
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('email', 'user_name')]),
        ),
    ]
