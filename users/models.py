from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from PIL import Image


class CustomUser(AbstractUser):
    cat = models.CharField(max_length=200)
    std = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=15)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return '{} Profile'.format(self.user.username)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
