from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'CustomUser'

    class Role(models.TextChoices):
        EMPLOYER = 'employer', 'Employer'
        WORKER = 'worker', 'Worker'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.EMPLOYER,
    )