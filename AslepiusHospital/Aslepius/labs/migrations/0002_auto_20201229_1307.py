# Generated by Django 3.0.5 on 2020-12-29 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labs_payment',
            name='cardnumber',
            field=models.BigIntegerField(),
        ),
    ]
