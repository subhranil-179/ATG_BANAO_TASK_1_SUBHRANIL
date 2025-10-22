from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    class Type(models.TextChoices):
        DOCTOR = "doctor", _("Doctor")
        PATIENT = "patient", _("Patient")
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False, unique=True)
    user_type = models.CharField(
        max_length=10,
        choices=Type.choices,
        default=Type.PATIENT,
        verbose_name="User Type"
    )

    def __str__(self):
        return self.username

class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses'
    )
    line_1 = models.CharField(max_length=256)
    city = models.CharField(max_length=72)
    state = models.CharField(max_length=72)
    pincode = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user}'s Address"
