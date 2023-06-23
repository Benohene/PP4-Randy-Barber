from django.db import models
from django.contrib.auth.models import User

TIME_CHOICES = (
    (0, "10AM"), (1, "11AM"), (2, "12AM"), (3, "1PM"), (4, "2PM"), (5, "3PM"), (6, "4PM"), (7, "5PM"), (8, "6PM"), (9, "7PM")
)

class Appointment(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")
    name = models.CharField(max_length=200)
    appointment_date = models.DateField()
    appointment_time = models.IntegerField(choices=TIME_CHOICES, default=0)
    phone_number = models.IntegerField()
    message = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['appointment_date', 'appointment_time']

    def __str__(self):
        return f"{self.user.name} | day: {self.appointment_date} | time: {self.appointment_time}"