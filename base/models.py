from xml.parsers.expat import model
from django.db import models

# Create your models here.
class Navlink(models.Model):
    text = models.CharField("text hiện ra trên menu", max_length=50)
    link = models.CharField("link của menu item", max_length=100)
    position = models.IntegerField("thứ tự menu", blank=True, default=0)
    #không cần field này nữa vì xử lý trong view luôn
    activated = models.BooleanField("cho biết đang ở trang nào", default=False)

    def __str__(self):
        return (str(self.position) + " : " + self.text + " : " + self.link)

class Testitem(models.Model):
    text = models.CharField("text hiện ra trên menu", max_length=50)
    activated = models.BooleanField("cho biết đang ở trang nào", default=False)

    def __str__(self):
        return (self.text + " - " + str(self.activated))