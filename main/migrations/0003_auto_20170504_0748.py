# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-04 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170504_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='place',
            field=models.CharField(choices=[('\u041d\u0410\u0420\u042b\u041d', '\u041d\u0410\u0420\u042b\u041d'), ('\u0418\u0441\u0441\u044b\u043a-\u041a\u0443\u043b\u044c', '\u0418\u0441\u0441\u044b\u043a-\u041a\u0443\u043b\u044c'), ('\u041e\u0428', '\u041e\u0428'), ('\u0411\u0430\u0442\u043a\u0435\u043d', '\u0411\u0430\u0442\u043a\u0435\u043d'), ('\u0422\u0430\u043b\u0430\u0441', '\u0422\u0430\u043b\u0430\u0441'), ('\u0414\u0436\u0430\u043b\u0430\u043b-\u0410\u0431\u0430\u0434', '\u0414\u0436\u0430\u043b\u0430\u043b-\u0410\u0431\u0430\u0434'), ('\u0427\u0443\u0439', '\u0427\u0443\u0439')], max_length=50, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c'),
        ),
    ]
