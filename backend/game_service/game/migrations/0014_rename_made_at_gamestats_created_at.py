# Generated by Django 5.1.1 on 2024-11-20 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_remove_gamestats_created_at_gamestats_made_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamestats',
            old_name='made_at',
            new_name='created_at',
        ),
    ]
