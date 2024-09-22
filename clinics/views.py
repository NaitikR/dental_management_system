from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Clinic, DoctorAffiliation
from django.http import JsonResponse
# Create your views here.

class ClinicListView(LoginRequiredMixin, ListView):
    model = Clinic
    context_object_name = 'clinics'

class ClinicDetailView(LoginRequiredMixin, DetailView):
    model = Clinic

class ClinicCreateView(LoginRequiredMixin, CreateView):
    model = Clinic
    fields = ['name', 'phone_number', 'email', 'address', 'city', 'state']
    success_url = reverse_lazy('clinic_list')

class ClinicUpdateView(LoginRequiredMixin, UpdateView):
    model = Clinic
    fields = ['name', 'phone_number', 'email', 'address', 'city', 'state']
    success_url = reverse_lazy('clinic_list')

class DoctorAffiliationCreateView(LoginRequiredMixin, CreateView):
    model = DoctorAffiliation
    fields = ['doctor', 'office_address', 'working_schedule']
    
    def form_valid(self, form):
        form.instance.clinic = Clinic.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('clinic_detail', kwargs={'pk': self.kwargs['pk']})

def get_clinics_by_procedure(request):
    if request.method == 'POST':
        procedure = request.POST.get('procedure')
        clinics = Clinic.objects.filter(doctor_affiliations__doctor__specialties__contains=[procedure]).distinct()
        data = {'clinics': [{'id': clinic.id, 'name': clinic.name} for clinic in clinics]}
        return JsonResponse(data)

def clinic_detail(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    affiliations = DoctorAffiliation.objects.filter(clinic=clinic)
    return render(request, 'clinics/clinic_detail.html', {
        'clinic': clinic,
        'affiliations': affiliations,
    })

def home(request):
    return render(request, 'home.html')