# Generated by Django 2.2.6 on 2019-10-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20191020_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
