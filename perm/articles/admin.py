from django.contrib import admin

from articles.models import Adv


@admin.register(Adv)
class AdvAdmin(admin.ModelAdmin):
    pass
