# Generated by Django 3.0.5 on 2020-09-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20200911_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='availability',
            name='timeslot1',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='availability',
            name='timeslot2',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='availability',
            name='timeslot3',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='availability',
            name='timeslot4',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='availability',
            name='timeslot5',
            field=models.CharField(max_length=15),
        ),
    ]