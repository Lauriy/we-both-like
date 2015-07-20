# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WeBothLikeWeb', '0003_auto_20150720_2137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswer',
            old_name='no',
            new_name='answer',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='yes',
        ),
    ]
