# Generated by Django 4.0.4 on 2023-06-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_count_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='short_URL',
            field=models.CharField(blank=True, max_length=7, null=True, unique=True),
        ),
    ]
