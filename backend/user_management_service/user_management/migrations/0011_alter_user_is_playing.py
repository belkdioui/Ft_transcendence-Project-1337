# Generated by Django 4.2.15 on 2024-09-15 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0010_user_friends_user_is_playing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_playing',
            field=models.CharField(blank=True, choices=[(None, None), ('pong', 'Pong'), ('space_invaders', 'Space Invaders'), ('road_fighter', 'Road Fighter')], max_length=255, null=True),
        ),
    ]
