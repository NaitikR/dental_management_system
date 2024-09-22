from rest_framework import generics
from .models import Patient, Visit, Appointment
from .serializers import PatientSerializer, VisitSerializer, AppointmentSerializer

class PatientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class VisitListCreateAPIView(generics.ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


