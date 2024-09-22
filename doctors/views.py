from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Doctor
from django.shortcuts import render, get_object_or_404
from patients.models import Patient

class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    context_object_name = 'doctors'

class DoctorDetailView(LoginRequiredMixin, DetailView):
    model = Doctor

class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    fields = ['npi', 'name', 'email', 'phone_number', 'specialties']
    success_url = reverse_lazy('doctor_list')

class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctor
    fields = ['npi', 'name', 'email', 'phone_number', 'specialties']
    success_url = reverse_lazy('doctor_list')

def get_doctors_by_clinic_and_procedure(request):
    clinic_id = request.GET.get('clinic')
    procedure = request.GET.get('procedure')
    doctors = Doctor.objects.filter(clinic_affiliations__clinic_id=clinic_id, specialties__contains=[procedure]).distinct()
    data = {'doctors': [{'id': doctor.id, 'name': doctor.name} for doctor in doctors]}
    return JsonResponse(data)

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    patients = Patient.objects.filter(visits__doctor=doctor).distinct()
    return render(request, 'doctors/doctor_detail.html', {
        'doctor': doctor,
        'patients': patients,
    })