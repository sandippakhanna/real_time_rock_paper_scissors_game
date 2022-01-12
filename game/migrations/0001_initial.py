# Generated by Django 4.0 on 2022-01-01 09:34

from django.db import migrations, models
import game.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.CharField(default=game.utils.get_id, editable=False, max_length=6, primary_key=True, serialize=False)),
                ('currentRound', models.IntegerField(blank=True, null=True)),
                ('user1', models.CharField(blank=True, max_length=6, null=True)),
                ('user2', models.CharField(blank=True, max_length=6, null=True)),
                ('user1Choice', models.CharField(blank=True, choices=[('Rock', 'rock'), ('Paper', 'paper'), ('Scissor', 'scissor')], max_length=10, null=True)),
                ('user2Choice', models.CharField(blank=True, choices=[('Rock', 'rock'), ('Paper', 'paper'), ('Scissor', 'scissor')], max_length=10, null=True)),
                ('user1Score', models.IntegerField(default=0)),
                ('user2Score', models.IntegerField(default=0)),
            ],
        ),
    ]