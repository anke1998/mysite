# Register your models here.
from django.contrib import admin
from .models import Readnum


@admin.register(Readnum)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_object')