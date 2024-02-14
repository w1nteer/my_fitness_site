from django.contrib import admin
from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('avatar',)}),  # Добавьте свои пользовательские поля
    )
    # Отобразить все поля в списке объектов
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)