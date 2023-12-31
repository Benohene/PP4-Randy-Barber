# Generated by Django 4.2.2 on 2023-06-23 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointment', '0002_delete_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.IntegerField(choices=[(0, '10AM'), (1, '11AM'), (2, '12AM'), (3, '1PM'), (4, '2PM'), (5, '3PM'), (6, '4PM'), (7, '5PM'), (8, '6PM'), (9, '7PM')], default=0)),
                ('phone_number', models.IntegerField()),
                ('message', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['appointment_date', 'appointment_time'],
            },
        ),
    ]
