# Generated by Django 2.2.7 on 2019-12-05 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0019_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hos_id', models.CharField(max_length=5)),
                ('p_name', models.CharField(max_length=5)),
                ('date', models.CharField(default='05/12/2019', max_length=100)),
                ('time', models.CharField(default='06:00:39', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='date',
            field=models.CharField(default='05/12/2019', max_length=100),
        ),
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.CharField(default='06:00:39', max_length=100),
        ),
    ]