# Generated by Django 3.1.4 on 2021-01-08 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0004_auto_20210108_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок поста'),
        ),
    ]
