# Generated by Django 2.1.5 on 2022-03-22 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Course',
        ),
    ]