from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# **kwargs--> https://www.youtube.com/watch?v=kB829ciAXo4&t=277s
# django signale--> https://www.youtube.com/watch?v=T6PyDm79PFo