# Generated by Django 4.1.2 on 2023-05-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_cartitems_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
