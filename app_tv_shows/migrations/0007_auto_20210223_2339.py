# Generated by Django 2.2.4 on 2021-02-24 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tv_shows', '0006_auto_20210223_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shows',
            name='releasedate_new',
        ),
        migrations.AlterField(
            model_name='shows',
            name='release_date',
            field=models.DateField(),
        ),
    ]
