# Generated by Django 3.0.8 on 2020-07-20 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Event Title')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('level', models.CharField(choices=[('ERROR', 'ERROR'), ('DEBUG', 'DEBUG'), ('WARING', 'WARING')], max_length=6, verbose_name='Level')),
                ('event_type', models.CharField(choices=[('D', 'Dev'), ('P', 'Produção'), ('H', 'Homologação')], max_length=1, verbose_name='Type')),
                ('error_date', models.DateField(auto_now_add=True, verbose_name='Error Date')),
                ('archived', models.BooleanField()),
                ('colected_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User', verbose_name='')),
            ],
            options={
                'db_table': 'events',
                'ordering': ['error_date'],
            },
        ),
    ]
