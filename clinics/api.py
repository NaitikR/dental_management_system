from rest_framework import generics
from .models import Clinic
from .serializers import ClinicSerializer


class ClinicListAPIView(generics.ListAPIView):
    serializer_class = ClinicSerializer

    def get_queryset(self):
        procedure = self.request.query_params.get('procedure')
        if procedure:
            return Clinic.objects.filter(doctor_affiliations__doctor__specialties__contains=[procedure]).distinct()
        return Clinic.objects.all()

class ClinicListCreateAPIView(generics.ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class ClinicDetailAPIView(generics.RetrieveAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer