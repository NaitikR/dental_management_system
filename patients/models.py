from django.db import models
from doctors.models import Doctor
from clinics.models import Clinic

class Patient(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    ssn_last_4 = models.CharField(max_length=4)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    procedures = models.JSONField()
    notes = models.TextField()

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    procedure = models.CharField(max_length=100)