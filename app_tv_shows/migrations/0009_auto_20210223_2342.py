# Generated by Django 2.2.4 on 2021-02-24 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tv_shows', '0008_auto_20210223_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shows',
            old_name='releasedate_new',
            new_name='release_date',
        ),
    ]
