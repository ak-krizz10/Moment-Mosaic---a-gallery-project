# Generated by Django 5.0.1 on 2024-01-20 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0007_alter_favourites_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourites',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.image'),
        ),
    ]
