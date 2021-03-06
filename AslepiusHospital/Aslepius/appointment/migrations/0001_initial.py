# Generated by Django 3.0.5 on 2020-09-08 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dept', '0002_departments_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('sno', models.IntegerField(primary_key=True, serialize=False)),
                ('timeslot1', models.TimeField()),
                ('timeslot2', models.TimeField()),
                ('timeslot3', models.TimeField()),
                ('timeslot4', models.TimeField()),
                ('timeslot5', models.TimeField()),
                ('dayunavailable1', models.CharField(max_length=10)),
                ('dayunavailable2', models.CharField(max_length=10)),
                ('doctorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept.Departments')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('aptid', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('doctorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept.Departments')),
                ('patientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
