# Generated by Django 2.2.6 on 2019-11-17 20:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_auto_20191110_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=100)),
                ('channel', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chats', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.CharField(max_length=100)),
                ('channel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=100)),
                ('channel', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='register',
            name='image_link',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='ph_no',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
