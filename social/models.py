from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)  # Asegura que el correo sea único
    password = models.CharField(max_length=128)  # Almacena contraseñas en formato seguro (encriptado en autenticación)
    nombre = models.CharField(max_length=50, default="Sin nombre")
    image = models.ImageField(default='batman.png')
    banner = models.ImageField(upload_to='banners/', blank=True, null=True)  # Imagen del banner
    educacion = models.TextField(blank=True, null=True)  # Información de educación
    habilidades = models.TextField(blank=True, null=True)  # Habilidades
    certificaciones = models.TextField(blank=True, null=True)  # Certificaciones

    def __str__(self):
        return f'{self.nombre} ({self.user.username})'



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()  # Descripción del post
    image = models.ImageField(upload_to='posts/', blank=True, null=True)  # Imagen opcional

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content[:50]}...'  # Muestra solo los primeros 50 caracteres