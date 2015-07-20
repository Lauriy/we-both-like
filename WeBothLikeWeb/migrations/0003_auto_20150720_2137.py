# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WeBothLikeWeb', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yes', models.BooleanField(default=False)),
                ('no', models.BooleanField(default=False)),
                ('question', models.ForeignKey(to='WeBothLikeWeb.Question')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='question',
            name='users',
            field=models.ManyToManyField(related_name='questions', through='WeBothLikeWeb.UserAnswer', to=settings.AUTH_USER_MODEL),
        ),
    ]
