# Generated by Django 3.0.8 on 2020-07-21 00:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200720_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]