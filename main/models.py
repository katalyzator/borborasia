# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode

PLACE_CHOICES = (
    ('НАРЫН', 'НАРЫН'),
    ('Иссык-Куль', 'Иссык-Куль'),
    ('ОШ', 'ОШ'),
    ('Баткен', 'Баткен'),
    ('Талас', 'Талас'),
    ('Джалал-Абад', 'Джалал-Абад'),
    ('Чуй', 'Чуй'),
)


class Tour(models.Model):
    class Meta:
        verbose_name_plural = 'Туры'
        verbose_name = 'Тур'

    name = models.CharField(max_length=1000, verbose_name='Наименование')
    place = models.CharField(choices=PLACE_CHOICES, verbose_name='Область', max_length=50)
    description = models.TextField(verbose_name='Описание Тура')
    text = models.TextField(verbose_name='Текст')
    main_image = models.ImageField(upload_to='tours/images', verbose_name='Главная картинка')
    youtube_video = models.CharField(max_length=255, verbose_name='Вставьте ссылку видео')

    def __unicode__(self):
        return smart_unicode(self.name)


class TourImage(models.Model):
    class Meta:
        verbose_name_plural = 'Фотографии Туров'
        verbose_name = 'Фотография Тура'

    tour = models.ForeignKey(Tour, verbose_name='Выберите тур')
    image = models.ImageField(upload_to='tours/images')

    def __unicode__(self):
        return smart_unicode(self.tour.name)


class Personal(models.Model):
    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'

    name = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=100, verbose_name='Позиция')
    image = models.ImageField(upload_to='personals/images', verbose_name='Фотография')

    def __unicode__(self):
        return smart_unicode(self.name)


class Vacancy(models.Model):
    class Meta:
        verbose_name_plural = 'Вакансии'
        verbose_name = 'Вакансия'

    position = models.CharField(max_length=255, verbose_name='Позиция')
    description = models.CharField(max_length=600, verbose_name='Описание')
    calary = models.IntegerField(default=10000, verbose_name='Зарплата')

    def __unicode__(self):
        return smart_unicode(self.description)
