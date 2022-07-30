from django.shortcuts import render
from .models import *


# xem trang home
def home(request):
    context = {
        "navs": Navlink.objects.order_by('position'),
        "current": "Home",
    }
    return render(request,'index.html',context)
