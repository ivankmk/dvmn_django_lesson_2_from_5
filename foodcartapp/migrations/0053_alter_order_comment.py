# Generated by Django 3.2 on 2021-10-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0052_alter_order_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, default='', max_length=510, verbose_name='Комментарий к заказу'),
        ),
    ]
