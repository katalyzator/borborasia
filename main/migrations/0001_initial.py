# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-08 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u0435\u0441\u0442\u0430')),
                ('person', models.CharField(max_length=255, verbose_name='\u0424\u0418\u041e')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('image', models.ImageField(blank=True, upload_to='feedback/images', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u041e\u0442\u0437\u044b\u0432',
                'verbose_name_plural': '\u041e\u0442\u0437\u044b\u0432\u044b',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u0424\u0418\u041e')),
                ('position', models.CharField(max_length=100, verbose_name='\u041f\u043e\u0437\u0438\u0446\u0438\u044f')),
                ('image', models.ImageField(upload_to='personals/images', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a',
                'verbose_name_plural': '\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
                ('place', models.CharField(choices=[('\u041d\u0410\u0420\u042b\u041d', '\u041d\u0410\u0420\u042b\u041d'), ('\u0418\u0441\u0441\u044b\u043a-\u041a\u0443\u043b\u044c', '\u0418\u0441\u0441\u044b\u043a-\u041a\u0443\u043b\u044c'), ('\u041e\u0428', '\u041e\u0428'), ('\u0411\u0430\u0442\u043a\u0435\u043d', '\u0411\u0430\u0442\u043a\u0435\u043d'), ('\u0422\u0430\u043b\u0430\u0441', '\u0422\u0430\u043b\u0430\u0441'), ('\u0414\u0436\u0430\u043b\u0430\u043b-\u0410\u0431\u0430\u0434', '\u0414\u0436\u0430\u043b\u0430\u043b-\u0410\u0431\u0430\u0434'), ('\u0427\u0443\u0439', '\u0427\u0443\u0439')], max_length=50, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0422\u0443\u0440\u0430')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('main_image', models.ImageField(upload_to='tours/images', verbose_name='\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('youtube_video', models.CharField(max_length=255, verbose_name='\u0412\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u0441\u0441\u044b\u043b\u043a\u0443 \u0432\u0438\u0434\u0435\u043e')),
                ('winter', models.BooleanField(default=False, verbose_name='(\u0417\u0418\u041c\u0410) \u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435 \u0435\u0441\u043b\u0438 \u044d\u0442\u043e\u0442 \u0442\u0443\u0440 \u043f\u043e\u0434\u0445\u043e\u0434\u0438\u0442 \u0434\u043b\u044f \u0437\u0438\u043c\u043d\u0435\u0433\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0430')),
                ('summer', models.BooleanField(default=False, verbose_name='(\u041b\u0415\u0422\u041e) \u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435 \u0435\u0441\u043b\u0438 \u044d\u0442\u043e\u0442 \u0442\u0443\u0440 \u043f\u043e\u0434\u0445\u043e\u0434\u0438\u0442 \u0434\u043b\u044f \u043b\u0435\u0442\u043d\u0435\u0433\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0422\u0443\u0440',
                'verbose_name_plural': '\u0422\u0443\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tours/images')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tour', verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0443\u0440')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0422\u0443\u0440\u0430',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u0422\u0443\u0440\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255, verbose_name='\u041f\u043e\u0437\u0438\u0446\u0438\u044f')),
                ('description', models.CharField(max_length=600, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('calary', models.IntegerField(default=10000, verbose_name='\u0417\u0430\u0440\u043f\u043b\u0430\u0442\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u044f',
                'verbose_name_plural': '\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438',
            },
        ),
    ]
