from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    birth_day = models.DateField(null=True)
    phone = models.CharField(max_length=11)

    def profil_sayac(self):
        return self.profile_set.all().count()