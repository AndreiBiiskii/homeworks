# Generated by Django 5.0 on 2024-01-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_alter_favorite_advertisement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.TextField(unique=True),
        ),
    ]