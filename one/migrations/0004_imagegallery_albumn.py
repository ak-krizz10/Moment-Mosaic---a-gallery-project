# Generated by Django 5.0.1 on 2024-01-20 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0003_remove_albumn_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagegallery',
            name='albumn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='one.albumn'),
        ),
    ]
