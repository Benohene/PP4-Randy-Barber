from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, CreateView
from .models import Appointment
from .forms import AppointmentForm
#from django.http import HttpResponse

class HomeView(TemplateView):
    """
    View to render homepage
    """
    template_name = 'index.html'

class ServiceView(TemplateView):
    """
    View to render service page
    """
    template_name = 'service.html'

class ContactView(TemplateView):
    """
    View to render contact page
    """
    template_name = 'contact.html'

class AppointmentView(LoginRequiredMixin, CreateView):
    """
    View to render appointment page
    """
    model = Appointment
    success_url = '/appointments/manage_appointment/'
    template_name = 'appointments/appointment.html'
    # success_msg = 'Flavor created.'
    fields = [
        'name', 'appointment_date', 'appointment_time', 'phone_number', 'message',
        ]

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)
