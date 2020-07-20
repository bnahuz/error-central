# Generated by Django 3.0.8 on 2020-07-20 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Event Title')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('level', models.CharField(choices=[('D', 'Dev'), ('P', 'Produção'), ('H', 'Homologação')], max_length=1, verbose_name='Level')),
                ('event_type', models.CharField(choices=[('D', 'Dev'), ('P', 'Produção'), ('H', 'Homologação')], max_length=1, verbose_name='Type')),
                ('error_date', models.DateField(auto_now_add=True, verbose_name='Error Date')),
                ('archived', models.BooleanField()),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
    ]
