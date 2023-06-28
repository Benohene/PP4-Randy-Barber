from django.shortcuts import render, get_object_or_404
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import Appointment
from .forms import AppointmentForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

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


class AppointmentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View to render appointment page 
    renders the view of the appointment forms
    """
    template_name = 'appointment.html'
    model = Appointment
    form_class = AppointmentForm
    success_url= reverse_lazy('user_panel')
    success_message = 'Appointment has successfully being booked!'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super(AppointmentView, self).form_valid(form)

    
class UserPanelView(LoginRequiredMixin, ListView):
    """
    View to render Userpanel page 
    to have access to already appointments booked
    to have access th the pade to edit and delete appointment
    """

    model = Appointment
    template_name = "user_panel.html"
    context_object_name = 'appointments'
    paginate_by = 2


    def get_queryset(self):
        if self.request.user.is_staff:
            return Appointment.objects.all()
        else:    
            return Appointment.objects.filter(customer=self.request.user)


class AppointmentEditView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    View to render appointment page 
    renders the view of the appointment forms for Update
    """
    model = Appointment
    template_name = 'appointment_edit.html'
    form_class = AppointmentForm
    success_url= reverse_lazy('user_panel')
    success_message = 'Appointment has successfully being edited!'

    def userUpdate(request, id):
        appointment = Appointment.objects.get(pk=id)

    def test_func(self):
        appointment = self.get_object()
        
        return self.request.user == appointment.customer


class AppointmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """
    View to render appointment page 
    renders the view of the appointment forms
    """
    template_name = 'appointment_confirm_delete.html'
    success_url = reverse_lazy('user_panel')
    context_object_name = 'appointment'
    queryset = Appointment.objects.all()
    success_message = 'Appointment has successfully being deleted!'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        appointments = self.get_context_data(object=self.object)
        return self.render_to_response(appointments)

    def test_func(self):
        appointment = self.get_object()
        return self.request.user == appointment.customer