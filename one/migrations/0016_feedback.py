# Generated by Django 5.0.1 on 2024-02-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0015_favourites_user_alter_image_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
