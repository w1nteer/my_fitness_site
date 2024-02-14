from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = models.CharField(max_length=255, verbose_name='URL', unique=True, null=True, blank=True)
    view_name = models.CharField(max_length=255, verbose_name='Название view', null=True)
    title_for_page = models.CharField(max_length=255, verbose_name='Заголовок для страницы', blank=True, null=True)

    def get_absolute_url(self):
        if self.slug is None:
            return reverse('home')
        
        return reverse(viewname=f'{self.view_name}')
        
    def __str__(self):
        return self.name