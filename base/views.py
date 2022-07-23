from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home page ne')

def contactus(request):
    return HttpResponse('contact us')