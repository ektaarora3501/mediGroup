# Generated by Django 2.2.7 on 2019-11-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0015_auto_20191121_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='channels',
            name='motto',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
