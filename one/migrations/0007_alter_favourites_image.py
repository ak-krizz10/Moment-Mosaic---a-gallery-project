# Generated by Django 5.0.1 on 2024-01-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0006_favourites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourites',
            name='image',
            field=models.ImageField(upload_to='favourites'),
        ),
    ]
