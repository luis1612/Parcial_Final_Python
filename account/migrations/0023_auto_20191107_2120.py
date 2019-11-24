# Generated by Django 2.2.6 on 2019-11-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_auto_20191103_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('public', 'Public_Account'), ('private', 'Private_Account')], default='public', max_length=80, null=True),
        ),
    ]
