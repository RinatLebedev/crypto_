# Generated by Django 4.1.3 on 2022-12-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_created=True, verbose_name='Дата обновления')),
                ('currency', models.CharField(max_length=4, verbose_name='Валюта')),
                ('RUB', models.FloatField(verbose_name='В рублях')),
                ('USDT', models.FloatField(verbose_name='В USDT')),
                ('volume', models.IntegerField(verbose_name='Объём')),
                ('change', models.FloatField(verbose_name='Изменение')),
                ('quote_volume', models.FloatField(verbose_name='Капитализация')),
            ],
        ),
    ]