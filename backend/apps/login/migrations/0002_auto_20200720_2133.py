# Generated by Django 3.0.8 on 2020-07-21 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='access_token',
            field=models.CharField(max_length=100),
        ),
    ]