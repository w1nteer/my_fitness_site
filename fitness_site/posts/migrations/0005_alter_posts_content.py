# Generated by Django 4.1 on 2023-06-24 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_posts_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(verbose_name='Текст поста'),
        ),
    ]