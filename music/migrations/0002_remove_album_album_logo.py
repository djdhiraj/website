# Generated by Django 2.1.7 on 2019-02-21 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_logo',
        ),
    ]