# Generated by Django 3.2 on 2021-10-16 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0049_rename_paymenth_method_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='restaraunt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaraunt_orders', to='foodcartapp.restaurant'),
        ),
    ]
