from django.db import models
# Create your models here.

class Doctor(models.Model):
    SPECIALTIES = [
        ('Cleaning', 'Cleaning'),
        ('Filling', 'Filling'),
        ('Root Canal', 'Root Canal'),
        ('Crown', 'Crown'),
        ('Teeth Whitening', 'Teeth Whitening'),
    ]

    npi = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    specialties = models.JSONField()

    def __str__(self):
        return self.name