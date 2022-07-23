from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'main.html')

def newhome(request):
    return render(request,'home.html')

def contactus(request):
    return HttpResponse('contact us')