from django.contrib import admin
from .models import DbUser, Spending


# Регистрация сущностей БД в панели администратора
@admin.register(DbUser)
class DbUser_admin(admin.ModelAdmin):
    list_display = ('id', 'vk_id', 'tg_id', 'site_id', 'token')  # Атрибуты, отображаемые в списке всех объектов


@admin.register(Spending)
class Spending_admin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'category', 'name', 'sum', 'common')  # атрибуты в списке объектов
