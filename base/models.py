from xml.parsers.expat import model
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30, help_text='Your name')
    email = models.EmailField(max_length=254, help_text='Your email')
    message = models.TextField(max_length=2000, help_text='Write here your message!')

    def __str__(self):
        return self.email

class CompanyInfo(models.Model):
    name = models.CharField("Tên công ty", max_length=50)
    phone = models.CharField("Điện thoại", max_length=50, blank=True)
    address = models.CharField("Địa chỉ", max_length=100, blank=True)
    email  = models.EmailField("Mail công ty", blank=True)
    facebook = models.URLField("Link facebook", max_length=128,  blank=True)
    linkedin = models.URLField("Link linkedin", max_length=128,  blank=True)
    twitter = models.URLField("Link twitter", max_length=128,  blank=True)
    
    def __str__(self):
        return self.name

class Navlink(models.Model):
    text = models.CharField("text hiện ra trên menu", max_length=50)
    link = models.CharField("link của menu item", max_length=100)
    position = models.IntegerField("thứ tự menu", blank=True, default=0)
    activated = models.BooleanField("cho biết đang ở trang nào", default=False) #không cần nữa vì xử lý trong view/context luôn

    def __str__(self):
        return (str(self.position) + " : " + self.text + " : " + self.link)

class Project(models.Model):
    name = models.CharField("Tên dự án", max_length=50)
    sumary = models.CharField("Tóm tắt", max_length=200, blank=True)  
    image  = models.CharField("Hình", max_length=128, blank=True)  

    def __str__(self):
        return self.name

class BoardMember(models.Model):
    name = models.CharField("Họ tên", max_length=50)
    title = models.CharField("Chức vụ", max_length=50)
    description = models.TextField("Thông tin")
    image  = models.CharField("Hình", max_length=128, blank=True)  

    def __str__(self):
        return self.name


class Testitem(models.Model):
    text = models.CharField("text hiện ra trên menu", max_length=50)
    image = models.ImageField("hình", blank=True)
    activated = models.BooleanField("cho biết đang ở trang nào", default=False)

    def __str__(self):
        return (self.text + " - " + str(self.activated))