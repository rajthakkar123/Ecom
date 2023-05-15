# Generated by Django 4.1.2 on 2022-11-24 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_options_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_society', models.CharField(max_length=255)),
                ('landmark', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
