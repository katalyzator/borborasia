# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-04 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170504_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='summer',
            field=models.BooleanField(default=False, verbose_name='(\u041b\u0415\u0422\u041e) \u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435 \u0435\u0441\u043b\u0438 \u044d\u0442\u043e\u0442 \u0442\u0443\u0440 \u043f\u043e\u0434\u0445\u043e\u0434\u0438\u0442 \u0434\u043b\u044f \u043b\u0435\u0442\u043d\u0435\u0433\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0430'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='winter',
            field=models.BooleanField(default=False, verbose_name='(\u0417\u0418\u041c\u0410) \u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435 \u0435\u0441\u043b\u0438 \u044d\u0442\u043e\u0442 \u0442\u0443\u0440 \u043f\u043e\u0434\u0445\u043e\u0434\u0438\u0442 \u0434\u043b\u044f \u0437\u0438\u043c\u043d\u0435\u0433\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0430'),
        ),
    ]