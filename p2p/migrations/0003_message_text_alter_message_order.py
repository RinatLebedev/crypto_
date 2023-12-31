# Generated by Django 4.1.3 on 2022-12-14 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p2p', '0002_alter_neworder_buy_post_alter_neworder_sell_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='text',
            field=models.TextField(default='', verbose_name='Текст'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='p2p.neworder', verbose_name='Ордер'),
        ),
    ]
