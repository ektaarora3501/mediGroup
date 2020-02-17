# Generated by Django 2.2.7 on 2020-01-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0023_auto_20200116_0725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channels',
            old_name='role',
            new_name='motto',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='motto',
            new_name='role',
        ),
        migrations.RemoveField(
            model_name='channels',
            name='username',
        ),
        migrations.AddField(
            model_name='members',
            name='username',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.CharField(default='07:29:46', max_length=100),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='time',
            field=models.CharField(default='07:29:46', max_length=100),
        ),
    ]