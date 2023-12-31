# Generated by Django 4.1.3 on 2022-12-14 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p2p', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neworder',
            name='buy_post',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='new_orders', to='p2p.buypost'),
        ),
        migrations.AlterField(
            model_name='neworder',
            name='sell_post',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='new_orders', to='p2p.sellpost'),
        ),
    ]
