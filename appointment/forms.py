from datetime import datetime
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django import forms
from .models import Appointment

#Added Appointment form class
class AppointmentForm(forms.ModelForm):
    """
    Form to create and edit a booking
    """
    class Meta:
        """ Set fields and labels """
        model = Appointment
        fields = [
            'name', 'appointment_date', 'appointment_time', 'phone_number', 'message',
            ]
        appointment_date = forms.DateField()
        labels = {
            'name': 'Name',
            'appointment_date' : 'Date - DD/MM/YY',
            'appointment_time' : 'Time',
            'phone_number' : 'Phone Number',
            'message' : 'Message',}
