# Generated by Django 2.2.7 on 2019-11-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0013_auto_20191121_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='otp',
            field=models.CharField(default=None, max_length=1),
        ),
    ]
