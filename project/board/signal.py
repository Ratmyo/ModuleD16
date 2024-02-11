from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserResponse


@receiver(post_save, sender=UserResponse)
def product_created(instance, **kwargs):
    print('Новый отклик!', instance)