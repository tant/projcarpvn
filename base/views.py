from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *


# xem trang home
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            # lưu database
            form.save()
            # gui mail nhap
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

            print(os.environ.get('SENDGRID_API_KEY'))

            message = Mail()
            message.to = [
                To(email=os.environ.get('TOE1'), name=os.environ.get('TON1') ),
                To(email=os.environ.get('TOE2'), name=os.environ.get('TON2') ),
                To(email=os.environ.get('TOE3'), name=os.environ.get('TON3') ),
            ]
            message.from_email = From(email=os.environ.get('FROME'), name=os.environ.get('FROMN'))
            message.subject = Subject("Khách kiếm trên website")

            message.content = [
                Content(
                    mime_type="text/html",
                    content="<p> Tên khách hàng: " + form.cleaned_data['name'] + "</p>" +
                        "<p> Email: " + form.cleaned_data['email'] + "</p>" +
                        "<p> Nội dung: " + form.cleaned_data['message'] + "</p>" 
                )
            ]

            response = sg.client.mail.send.post(request_body=message.get())

            #print(response.status_code)
            #print(response.body)
            #print(response.headers)

            print("chay duoc toi day")

            messages.info(request,'Message sent. We will contact you very at your email.')
        else:
            messages.info('Error sending your message.')

    context = {
        "navs": Navlink.objects.order_by('position'),
        "current": "Home",
        "form": ContactForm(),
    }

    return render(request, 'index.html', context)

    