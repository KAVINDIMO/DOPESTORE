# Generated by Django 3.1.3 on 2021-08-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210806_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderer',
            name='landmark',
            field=models.CharField(default='landmark', max_length=500),
        ),
    ]
