# Generated by Django 4.2.1 on 2023-05-30 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0008_comment_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.video'),
        ),
    ]