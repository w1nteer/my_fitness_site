# Generated by Django 4.1 on 2023-06-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.CharField(max_length=255, null=True, unique=True, verbose_name='URL')),
                ('view_name', models.CharField(max_length=255, null=True, verbose_name='Название view')),
                ('title_for_page', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок для страницы')),
            ],
        ),
    ]