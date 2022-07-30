from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# xem trang home
def home(request):
    return render(request,'home.html')

# xem trang home mới
def main(request):
    return render(request,'main.html')

def contactus(request):
    return HttpResponse('contact us')