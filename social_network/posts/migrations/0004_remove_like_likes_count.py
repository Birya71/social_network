# Generated by Django 5.0.3 on 2024-05-25 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_like_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='likes_count',
        ),
    ]
