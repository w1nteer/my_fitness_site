from django.contrib import admin
from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'slug', 'time_create', 'cat')
    list_display_links = ('title', )
    search_fields = ('title', 'content')
    list_filter = ('time_create', )
    prepopulated_fields = {'slug': ('title', )}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', )
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Posts, PostsAdmin)
