# Generated by Django 3.2 on 2021-10-24 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0055_alter_order_registered_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_status',
            new_name='status',
        ),
    ]