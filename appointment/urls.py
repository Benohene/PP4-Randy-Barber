from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="home"),path('', views.home, name="home"),
    path('service/', views.service, name="service"),
    path('contact/', views.contact, name="contact"),
    path('appointment/', views.appointment, name="appointment"),
]
