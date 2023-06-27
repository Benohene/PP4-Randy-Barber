from datetime import datetime
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django import forms
from .models import Appointment

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
            'message' : 'Message',
        }

    # def clean(self):
    #     """

    #     """
    #     date = self.cleaned_data['appointment_date']
    #     time = self.cleaned_data['appointment_time']
    #     # Throw validation errors on form
    #     if date < datetime.today().date():
    #         raise ValidationError(
    #             'Invalid date - Booking cannot be in the past')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['appointment_date'].widget.attrs['class'] = 'datepicker'
    #     self.fields['appointment_date'].widget.attrs['autocomplete'] = 'off'