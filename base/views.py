from django.shortcuts import render
from .models import *
from .forms import *


# xem trang home
def home(request):
    context = {
        "navs": Navlink.objects.order_by('position'),
        "current": "Home",
        "form": ContactForm(),
    }
    return render(request,'index.html',context)

def test(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    
    context = {
        "navs": Navlink.objects.order_by('position'),
        "current": "Home",
        "form": form,
    }

    return render(request, 'test.html', context)