# Generated by Django 2.2.12 on 2020-08-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200826_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default='', max_length=11),
        ),
    ]