from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Verifica que no haya otro perfil con el mismo correo antes de crear uno nuevo
        if Profile.objects.filter(user__email=instance.email).exists():
            print("Ya existe un perfil con este correo electrónico.")
            return
        
        Profile.objects.create(user=instance)