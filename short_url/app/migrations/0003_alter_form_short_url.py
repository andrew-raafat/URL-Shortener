# Generated by Django 4.0.4 on 2023-06-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_form_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='short_URL',
            field=models.CharField(max_length=7, unique=True),
        ),
    ]
