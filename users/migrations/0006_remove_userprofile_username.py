# Generated by Django 4.2.1 on 2023-05-30 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userprofile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]
