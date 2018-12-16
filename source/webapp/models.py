from django.db import models

# Create your models here.

class User(models.Model):
    nickname = models.CharField(max_length=50, verbose_name='Никнейм')
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    favorites = models.ManyToManyField('Article', blank=True, related_name='favored_by', verbose_name='Избранное')

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(max_length=2000, verbose_name='Содержание статьи')
    author = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
