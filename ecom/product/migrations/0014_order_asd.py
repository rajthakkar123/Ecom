# Generated by Django 4.1.2 on 2023-05-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_rename_order_orderitems_main_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='asd',
            field=models.CharField(default='asd', max_length=25),
            preserve_default=False,
        ),
    ]
