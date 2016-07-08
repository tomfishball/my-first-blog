# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(max_length=100, default='DEFAULT VALUE'),
        ),
    ]
