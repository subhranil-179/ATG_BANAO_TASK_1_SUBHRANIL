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
    # Address related fileds
    line_1 = models.CharField(max_length=256, null=True, verbose_name="Address Line 1")
    city = models.CharField(max_length=72, null=True)
    state = models.CharField(max_length=72, null=True)
    pincode = models.CharField(max_length=50, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=False)

    def __str__(self):
        return self.username
