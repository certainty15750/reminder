# Generated by Django 3.1.5 on 2021-01-21 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20210121_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appointment',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
