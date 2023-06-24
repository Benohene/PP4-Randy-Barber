from django.urls import path
from . import views
from appointment.views import HomeView, ServiceView, ContactView, AppointmentView



urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),path('', HomeView.as_view(), name="home"),
    path('service/', ServiceView.as_view(), name="service"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('appointment/', AppointmentView.as_view(), name="appointment"),
]


