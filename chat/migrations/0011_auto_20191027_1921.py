# Generated by Django 2.2.6 on 2019-10-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_message_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.IntegerField(choices=[(1, 'Sent'), (2, 'Seen')], default=1),
        ),
    ]
