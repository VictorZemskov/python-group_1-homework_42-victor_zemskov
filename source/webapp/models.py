from django.db import models

# Create your models here.

class User(models.Model):
    nickname = models.CharField(max_length=50, verbose_name='Никнейм')
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'