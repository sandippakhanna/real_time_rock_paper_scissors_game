# Generated by Django 4.0 on 2022-01-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_room_user1choice_alter_room_user2choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='user1Choice',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='user2Choice',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
