# Generated by Django 4.1.9 on 2023-12-04 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_feepayment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fee',
        ),
        migrations.AddField(
            model_name='course',
            name='totalfee',
            field=models.IntegerField(default=0),
        ),
    ]
