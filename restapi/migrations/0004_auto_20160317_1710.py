# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_auto_20160317_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('user_id',)},
        ),
    ]
