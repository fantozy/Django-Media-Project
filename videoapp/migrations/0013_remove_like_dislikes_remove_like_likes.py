# Generated by Django 4.2.1 on 2023-06-04 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0012_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='like',
            name='likes',
        ),
    ]
