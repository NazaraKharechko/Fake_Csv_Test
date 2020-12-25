# Generated by Django 3.1.4 on 2020-12-25 19:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ful_name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^([0])(\\d{9})$', 'not valid phone number')])),
                ('description', models.CharField(blank=True, default='', max_length=500)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'компанії',
                'verbose_name_plural': 'компанія',
                'db_table': 'company',
            },
        ),
    ]
