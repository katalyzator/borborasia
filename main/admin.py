from django.contrib import admin

from .models import *


class PersonalAdmin(admin.ModelAdmin):
    class Meta:
        model = Personal


admin.site.register(Personal, PersonalAdmin)
