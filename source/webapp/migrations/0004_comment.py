# Generated by Django 2.1 on 2018-12-16 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20181216_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=2000, verbose_name='Содержание комментария')),
                ('article', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='webapp.Article', verbose_name='Статья')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.User', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
