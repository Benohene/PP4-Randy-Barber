from django.shortcuts import render, get_object_or_404
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
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
    renders the view of the appointment forms
    """
    template_name = 'appointment.html'
    form_class = AppointmentForm
    success_url= reverse_lazy('user_panel')

    


class UserPanelView(LoginRequiredMixin, ListView):
    """
    View to render Userpanel page 
    to have access to already appointments booked
    to have access th the pade to edit and delete appointment
    """

    model = Appointment
    template_name = "user_panel.html"
    context_object_name = 'appointments'
    paginate_by = 4
    queryset = Appointment.objects.all()

    def get_queryset(self):
        return Appointment.objects.all()


class AppointmentEditView(LoginRequiredMixin, UpdateView):
    """
    View to render appointment page 
    renders the view of the appointment forms
    """
    model = Appointment
    template_name = 'appointment_edit.html'
    form_class = AppointmentForm
    success_url= reverse_lazy('user_panel')

    def userUpdate(request, id):
        appointment = Appointment.objects.get(pk=id)

    # def test_func(self):
    #     appointment = self.get_object()
    #     if self.request.user.id:
    #         return True
    #     return False