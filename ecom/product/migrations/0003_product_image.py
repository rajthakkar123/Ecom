# Generated by Django 4.1.2 on 2022-11-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_category_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='empty', upload_to='images/'),
            preserve_default=False,
        ),
    ]
