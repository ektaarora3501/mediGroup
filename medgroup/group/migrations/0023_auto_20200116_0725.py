# Generated by Django 2.2.7 on 2020-01-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0022_auto_20191216_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channels',
            old_name='creator',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='channels',
            old_name='motto',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='members',
            new_name='motto',
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.CharField(default='16/01/2020', max_length=100),
        ),
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.CharField(default='07:25:16', max_length=100),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='date',
            field=models.CharField(default='16/01/2020', max_length=100),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='time',
            field=models.CharField(default='07:25:16', max_length=100),
        ),
        migrations.AlterField(
            model_name='members',
            name='channel',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]