# Generated by Django 5.1.1 on 2024-09-22 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_game_match_alter_gamestats_game_type_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Game_Match',
            new_name='Game_History',
        ),
    ]