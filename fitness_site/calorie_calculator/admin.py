from django.contrib import admin
from .models import *


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name', )
    search_fields = ('title', )
    

admin.site.register(Menu, MenuAdmin)
