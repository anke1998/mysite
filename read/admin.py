# Register your models here.
from django.contrib import admin
from .models import Readnum, ReadDetail


@admin.register(Readnum)
class ReadAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_object')


@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('date', 'read_num', 'content_object')