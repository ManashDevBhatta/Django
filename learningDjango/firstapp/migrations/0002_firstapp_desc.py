# Generated by Django 5.1.6 on 2025-02-24 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstapp',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
