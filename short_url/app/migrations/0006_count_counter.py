# Generated by Django 4.0.4 on 2023-06-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_count_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='count',
            name='counter',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
