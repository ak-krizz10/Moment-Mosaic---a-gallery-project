# Generated by Django 5.0.1 on 2024-01-25 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0013_profile_vaultpin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='vaultpin',
        ),
    ]
