from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Этот модуль отвечает за создание БД

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновлеия')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Заглавное изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')



    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_at']



class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Наименование категории')


    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})



    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категориии'
        ordering = ['title']

    def __str__(self):
        return self.title


class Marker(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    id_news = models.ForeignKey('News', on_delete=models.CASCADE, verbose_name='Новость')
    marker = models.BooleanField(verbose_name='Отметка об ознакомлении')
    date_marker = models.DateTimeField(auto_now_add=True, verbose_name='Дата ознакомления')
    comment = models.TextField(blank=True, verbose_name='Примечание')

    class Meta:
        verbose_name = 'Отметка пользователя'
        verbose_name_plural = 'Отметки пользователя'
        ordering = ['id_user', 'date_marker']



