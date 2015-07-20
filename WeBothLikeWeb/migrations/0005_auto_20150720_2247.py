# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('WeBothLikeWeb', '0004_auto_20150720_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 20, 22, 47, 17, 202134, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useranswer',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 20, 22, 47, 24, 233031, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
