# Generated by Django 4.1.7 on 2023-04-30 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nftimage',
            name='currency',
            field=models.CharField(choices=[('USDT', 'usdt'), ('BTC', 'btc'), ('ETH', 'eth'), ('KPFU', 'kpfu'), ('SOL', 'sol')], max_length=4, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='nftpost',
            name='currency',
            field=models.CharField(choices=[('USDT', 'usdt'), ('BTC', 'btc'), ('ETH', 'eth'), ('KPFU', 'kpfu'), ('SOL', 'sol')], max_length=4, verbose_name='Валюта'),
        ),
    ]
