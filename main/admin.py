from django.contrib import admin
from modeltranslation.admin import TabbedExternalJqueryTranslationAdmin
from modeltranslation.translator import TranslationOptions, translator

from .models import *


class TourTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'text')


translator.register(Tour, TourTranslationOptions)


class PersonalAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']


class TourAdmin(TabbedExternalJqueryTranslationAdmin):
    class Meta:
        model = Tour

    list_display = ['name', 'place']


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['position', 'description']


class TourImageAdmin(admin.ModelAdmin):
    list_display = ['tour']


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['title', 'person']


admin.site.register(Feedback, FeedbackAdmin)

admin.site.register(TourImage, TourImageAdmin)

admin.site.register(Vacancy, VacancyAdmin)

admin.site.register(Tour, TourAdmin)

admin.site.register(Personal, PersonalAdmin)
