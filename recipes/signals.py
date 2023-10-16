from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from recipes.models import Recipe


@receiver(post_save,sender=Recipe)
def create_profile(sender,instance,created, *args, **kwargs):
    ...