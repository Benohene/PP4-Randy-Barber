from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home),
    path('service/', views.service),
    path('contact/', views.contact),
]
