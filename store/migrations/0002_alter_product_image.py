# Generated by Django 4.1.5 on 2023-01-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(upload_to='uploads/productsimage/'),
        ),
    ]
