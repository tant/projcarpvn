from django.shortcuts import render, redirect
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

            mail_from = From("tantran@carp.vn")
            mail_to = To("txntan@gmail.com")
            mail_subject = "Sending with SendGrid is Fun"
            mail_content = Content("text/plain", "and easy to do anywhere, even with Python")
            mail = Mail(mail_from, mail_to, mail_subject, mail_content)
            
            response = sg.client.mail.send.post(request_body=mail.get())

            print(response.status_code)
            print(response.body)
            print(response.headers)
            
            return redirect('/#contactus')
        else:
            print("khong valid")
            return redirect('/test')

    context = {
        "navs": Navlink.objects.order_by('position'),
        "current": "Home",
        "form": ContactForm(),
    }

    return render(request, 'index.html', context)

    