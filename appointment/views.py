from django.shortcuts import render
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, CreateView
from .models import Appointment
from .forms import AppointmentForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

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
    success_url=reverse_lazy('home')
    template_name = 'appointment.html'
    fields = [
        'name', 'appointment_date', 'appointment_time', 'phone_number', 'message',
        ]
    def form_valid(self, form):
         form.instance.created_by = self.request.user
    #     # messages.success(
    #     #     self.request,
    #     #     f'Booking confirmed for {guests} guests on {date}'
    #     # )

         return super(AppointmentView, self).form_valid(form)    
    # def get(self, request,*args):
    #     self.object = None
    #     return super().get(request, *args)

    # def post(self, request,*args):
    #     self.object = None
    #     return super().post(request, *args)