# Generated by Django 3.1.3 on 2021-08-13 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20210813_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderer',
            name='contactno',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
