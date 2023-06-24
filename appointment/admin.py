from django.contrib import admin
from .models import Appointment

# Register your models here.

@admin.register (Appointment)

class Appointment(admin.ModelAdmin):
    list_display = ('name', 'appointment_date', 'appointment_time', 'phone_number', 'message')
    search_fields = ['name', 'appointment_date']
    list_filter = ('appointment_time', ('appointment_date'))