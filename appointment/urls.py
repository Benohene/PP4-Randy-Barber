from django.urls import path
from . import views
from appointment.views import HomeView, ServiceView, ContactView 
from appointment.views import AppointmentView, UserPanelView


urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),path('', HomeView.as_view(), name="home"),
    path('service/', ServiceView.as_view(), name="service"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('appointment/', AppointmentView.as_view(), name="appointment"),
    path('user_panel/', UserPanelView.as_view(), name="user_panel"),
]


