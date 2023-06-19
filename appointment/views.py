from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')
# Create your views here.
