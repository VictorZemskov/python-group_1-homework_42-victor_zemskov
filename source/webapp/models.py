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
    author = models.ForeignKey('User', on_delete=models.PROTECT, related_name='articles', verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey('Article', null=True, blank=True, on_delete=models.PROTECT, related_name='comments', verbose_name='Статья')
    user = models.ForeignKey('User', on_delete=models.PROTECT, related_name='comments', verbose_name='Пользователь')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT, related_name='comments', verbose_name='Ответ на комментарий')
    content = models.TextField(max_length=2000, verbose_name='Содержание комментария')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Ratting(models.Model):
    MARK_TERRIBLE = 'terrible'
    MARK_BAD = 'bad'
    MARK_OK = 'ok'
    MARK_GOOD = 'good'
    MARK_FINE = 'fine'

    MARK_CHOICES = (
        (MARK_TERRIBLE, 'Ужасно'),
        (MARK_BAD, 'Плохо'),
        (MARK_OK, 'Нормально'),
        (MARK_GOOD, 'Хорошо'),
        (MARK_FINE, 'Отлично')
    )
    article = models.ForeignKey('Article', on_delete=models.PROTECT, related_name='rattings', verbose_name='Статья')
    user = models.ForeignKey('User', on_delete=models.PROTECT, related_name='rattings', verbose_name='Пользователь')
    mark = models.CharField(max_length=20, choices=MARK_CHOICES, verbose_name='Оценка')

    def __str__(self):
        return self.mark

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
