# Generated by Django 5.1.1 on 2024-11-20 20:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_gamestats_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamestats',
            name='created_at',
        ),
        migrations.AddField(
            model_name='gamestats',
            name='made_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]