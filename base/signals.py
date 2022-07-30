from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)


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
        logger.warning("Đã đổi status xong " + instance.text + "---- " + str(instance.pk))
    else:
        logger.warning("Mới tạo " + instance.text + "---- " + str(instance.pk))
