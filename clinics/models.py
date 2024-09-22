from django.db import models

# Create your models here.

class Clinic(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DoctorAffiliation(models.Model):
    clinic = models.ForeignKey('Clinic', on_delete=models.CASCADE, related_name='doctor_affiliations')
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='clinic_affiliations')
    office_address = models.TextField()
    working_schedule = models.TextField()

    class Meta:
        unique_together = ('clinic', 'doctor')