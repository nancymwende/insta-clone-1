# Generated by Django 4.0.5 on 2022-06-06 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0007_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
