from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def service(request):
    return HttpResponse('service')

def contact(request):
    return HttpResponse('contact')
# Create your views here.
