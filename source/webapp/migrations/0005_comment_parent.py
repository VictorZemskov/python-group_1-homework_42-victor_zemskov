# Generated by Django 2.1 on 2018-12-16 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='webapp.Comment', verbose_name='Ответ на комментарий'),
            preserve_default=False,
        ),
    ]