# Generated by Django 4.1.2 on 2023-05-09 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_cartitems_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='item_quantity',
        ),
    ]