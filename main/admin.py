from django.contrib import admin

from .models import *


class PersonalAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']


class TourAdmin(admin.ModelAdmin):
    list_display = ['name', 'place']


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['position', 'description']


class TourImageAdmin(admin.ModelAdmin):
    list_display = ['tour']


admin.site.register(TourImage, TourImageAdmin)

admin.site.register(Vacancy, VacancyAdmin)

admin.site.register(Tour, TourAdmin)

admin.site.register(Personal, PersonalAdmin)
