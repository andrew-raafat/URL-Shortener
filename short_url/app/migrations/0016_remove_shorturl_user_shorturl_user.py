# Generated by Django 4.0.4 on 2023-07-01 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0015_alter_shorturl_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='user',
        ),
        migrations.AddField(
            model_name='shorturl',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]