# Generated by Django 2.2.6 on 2019-10-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0013_auto_20191030_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='deletefor',
            field=models.IntegerField(blank=True, choices=[(1, 'DELETED for user01'), (2, 'DELETED for user02')], null=True),
        ),
    ]
