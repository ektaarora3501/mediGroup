# Generated by Django 2.2.7 on 2019-11-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0012_register_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='otp',
            field=models.BooleanField(),
        ),
    ]
