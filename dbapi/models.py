from django.db import models
from django.utils import timezone
from django.urls import reverse

from . import strings


class DbUser(models.Model):
    id = models.AutoField(primary_key=True)
    vk_id = models.CharField(max_length=50, blank=True, verbose_name="ключ вк")
    tg_id = models.CharField(max_length=50, blank=True, verbose_name="ключ телеграм")
    site_id = models.CharField(max_length=50, blank=True, verbose_name="ключ пользователя с сайта")
    token = models.CharField(max_length=100, blank=True, verbose_name="токен")


class Spending(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(DbUser, on_delete=models.CASCADE, related_name='spends', verbose_name="пользователь")
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата")
    category = models.CharField(max_length=50, choices=strings.CATEGORY_CHOICES, verbose_name="категория траты")
    name = models.CharField(max_length=100, verbose_name="наименование траты")
    sum = models.IntegerField(verbose_name="сумма траты")
    common = models.BooleanField(default=False, verbose_name="является ли расход общим в семье")
