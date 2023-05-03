from django.contrib import admin
from content.models import *
from django.db.models import QuerySet


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created_at']
    list_display_links = ['name', 'user']
    list_per_page = 5
    search_fields = ['name', ]
    ordering = ['-id', ]
