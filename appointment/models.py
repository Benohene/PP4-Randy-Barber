from django.db import models
from datetime import date
from django.contrib.auth.models import User

TIME_CHOICES = (
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
)

class Appointment(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer", null=True, blank=True)
    name = models.CharField(max_length=400)
    appointment_date = models.DateField()
    appointment_time = models.CharField(choices=TIME_CHOICES)
    phone_number = models.CharField(max_length=15)
    message = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['appointment_date', 'appointment_time']


    
