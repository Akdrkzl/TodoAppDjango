from django.contrib import admin
from .models import *

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('todo','user')
    readonly_fields = ('slug',)
admin.site.register(Todo,TodoAdmin)