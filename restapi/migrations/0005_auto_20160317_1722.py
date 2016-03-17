# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import restapi.models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0004_auto_20160317_1710'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', restapi.models.UserManager()),
            ],
        ),
    ]
