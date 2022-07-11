# Generated by Django 3.2 on 2021-10-16 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0050_order_restaraunt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='restaraunt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaraunt_orders', to='foodcartapp.restaurant', verbose_name='ресторан'),
        ),
    ]
