# Generated by Django 3.2 on 2021-10-14 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0046_auto_20211014_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='called_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivered_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
