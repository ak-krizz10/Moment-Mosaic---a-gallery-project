# Generated by Django 5.0.1 on 2024-01-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0008_alter_favourites_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumn',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
