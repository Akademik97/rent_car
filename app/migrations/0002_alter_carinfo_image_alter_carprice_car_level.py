# Generated by Django 5.0.7 on 2024-07-18 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='data/images/', verbose_name='Зображення автомобіля'),
        ),
        migrations.AlterField(
            model_name='carprice',
            name='car_level',
            field=models.CharField(max_length=256, verbose_name='Клас автомобіля'),
        ),
    ]
