from django.contrib import admin

from .models import *


class PersonalAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']


admin.site.register(Personal, PersonalAdmin)
