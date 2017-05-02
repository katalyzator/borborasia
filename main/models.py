# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode


class Tour(models.Model):
    class Meta:
        verbose_name_plural = 'Туры'
        verbose_name = 'Тур'

    name = models.CharField(max_length=1000, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание Тура')
    text = models.TextField(verbose_name='Текст')
    main_image = models.ImageField(upload_to='tours/images', verbose_name='Главная картинка')

    def __unicode__(self):
        return smart_unicode(self.name)


class Personal(models.Model):
    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'

    name = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=100, verbose_name='Позиция')
    image = models.ImageField(upload_to='personals/images', verbose_name='Фотография')

    def __unicode__(self):
        return smart_unicode(self.name)
