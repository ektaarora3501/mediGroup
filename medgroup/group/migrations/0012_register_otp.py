# Generated by Django 2.2.7 on 2019-11-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0011_auto_20191117_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='otp',
            field=models.BooleanField(default=False),
        ),
    ]