from django.forms import ModelForm, TextInput
from .models import Contact
# thêm captcha
from captcha.fields import CaptchaField

class ContactForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'
        