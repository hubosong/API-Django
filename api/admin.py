# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# used to search db data
from .models import Pictures

# used to show db items at Admin Painel
class PicturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name')
    list_per_page = 10
admin.site.register(Pictures, PicturesAdmin)
