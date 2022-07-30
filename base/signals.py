from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Navlink)
def Keep1activated(sender, instance, created, **kwargs):
    if (instance.activated):
        for item in Testitem.objects.all():
            if (item.pk != instance.pk):
                item.activated = False
                item.save()
    

@receiver(post_save, sender=Testitem)
def thongbao(sender, instance, created, **kwargs):
    if (instance.activated):
        for item in Testitem.objects.all():
            if (item.pk != instance.pk):
                item.activated = False
                item.save()
        print("Đã đổi tên anh em xong ", instance, "---- ", instance.pk)
    else:
        print("Mới tạo ", instance, "---- ", instance.pk)
