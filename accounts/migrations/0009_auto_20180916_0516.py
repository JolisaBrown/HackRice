# Generated by Django 2.0 on 2018-09-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180916_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='accountID',
            field=models.CharField(max_length=24),
        ),
    ]