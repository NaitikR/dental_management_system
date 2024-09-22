from rest_framework import serializers
from .models import Patient, Visit, Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'date_of_birth', 'address', 'phone_number', 'ssn_last_4', 'gender']

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'patient', 'doctor', 'clinic', 'date_time', 'procedures', 'notes']

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'clinic', 'date_time', 'procedure']