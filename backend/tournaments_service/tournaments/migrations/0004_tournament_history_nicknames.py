# Generated by Django 5.1.1 on 2024-11-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_remove_tournament_history_last_game_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament_history',
            name='Nicknames',
            field=models.JSONField(default=dict),
        ),
    ]