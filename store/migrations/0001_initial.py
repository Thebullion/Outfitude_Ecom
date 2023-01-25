# Generated by Django 4.1.5 on 2023-01-25 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=53)),
                ('Price', models.IntegerField(default=0)),
                ('Description', models.CharField(default='', max_length=200)),
                ('Image', models.ImageField(upload_to='productsimage/')),
            ],
        ),
    ]