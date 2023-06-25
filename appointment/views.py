from django.shortcuts import render, get_object_or_404, reverse
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, CreateView, ListView
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
    model = Appointment
    template_name = 'appointment.html'
    success_url=reverse_lazy('home')
    fields = [
        'name', 'appointment_date', 'appointment_time', 'phone_number', 'message',
        ]
    
    def form_valid(self, form):
         form.instance.created_by = self.request.user
         return super(AppointmentView, self).form_valid(form)    


class UserPanelView(LoginRequiredMixin, ListView):
    """
    View to render Userpanel page 
    to have access to already appointments booked
    to have access th the pade to edit and delete appointment
    """
    # template_name = reverse_lazy("user_panel.html")
    # model = Appointment
    # #template_name = 'user_panel.html'
    # paginate_by = 3

    # def get(self, request, *args, **kwargs):
    #     queryset = Appointment.objects.filter()
    #     appointments = get_object_or_404(queryset)
    #     return render (request, template_name)

    model = Appointment
    template_name = "user_panel.html"
    context_object_name = 'appointments'
    paginate_by = 4
    queryset = Appointment.objects.all()

    def get_queryset(self):
        return Appointment.objects.all()


    # model = Appointment
    # template_name = 'book-detail.html'
    # context_object_name = 'book'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     post = Books.objects.filter(slug=self.kwargs.get('slug'))
    #     post.update(count=F('count') + 1)

    #     context['time'] = timezone.now()

    #     return context