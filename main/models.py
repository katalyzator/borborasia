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
    winter = models.BooleanField(default=False,
                                 verbose_name='(ЗИМА) Отметьте если этот тур подходит для зимнего периода')
    summer = models.BooleanField(default=False,
                                 verbose_name='(ЛЕТО) Отметьте если этот тур подходит для летнего периода')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class TourImage(models.Model):
    class Meta:
        verbose_name_plural = 'Фотографии Туров'
        verbose_name = 'Фотография Тура'

    tour = models.ForeignKey(Tour, verbose_name='Выберите тур')
    image = models.ImageField(upload_to='tours/images')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.tour.name)


class Personal(models.Model):
    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'

    name = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=100, verbose_name='Позиция')
    image = models.ImageField(upload_to='personals/images', verbose_name='Фотография')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class Vacancy(models.Model):
    class Meta:
        verbose_name_plural = 'Вакансии'
        verbose_name = 'Вакансия'

    position = models.CharField(max_length=255, verbose_name='Позиция')
    description = models.CharField(max_length=600, verbose_name='Описание')
    calary = models.IntegerField(default=10000, verbose_name='Зарплата')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.description)


class Feedback(models.Model):
    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'

    title = models.CharField(max_length=255, verbose_name='Название места')
    person = models.CharField(max_length=255, verbose_name='ФИО')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='feedback/images', verbose_name='Фотография', blank=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)
