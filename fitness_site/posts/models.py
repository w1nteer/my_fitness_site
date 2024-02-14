from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from fitness_site.settings import AUTH_USER_MODEL
from registration.models import CustomUser


class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст поста')
    description = models.CharField(max_length=255, verbose_name='Краткое описание статьи')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Картинка', null=True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=False)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
        ordering = ['-time_create', '-title']


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})



class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', db_index=True)    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Comment(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.CASCADE, verbose_name='Пост')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Автор')
    content = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']