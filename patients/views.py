from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Patient, Visit, Appointment
from doctors.models import Doctor
from clinics.models import Clinic

class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'patients/patient_list.html'

class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'patients/patient_detail.html'

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    fields = ['name', 'date_of_birth', 'address', 'phone_number', 'ssn_last_4', 'gender']
    success_url = reverse_lazy('patient_list')
    template_name = 'patients/patient_form.html'

class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    fields = ['name', 'date_of_birth', 'address', 'phone_number', 'ssn_last_4', 'gender']
    success_url = reverse_lazy('patient_list')
    template_name = 'patients/patient_form.html'

class VisitCreateView(LoginRequiredMixin, CreateView):
    model = Visit
    fields = ['doctor', 'clinic', 'date_time', 'procedures', 'notes']
    template_name = 'patients/visit_form.html'
    
    def form_valid(self, form):
        form.instance.patient = get_object_or_404(Patient, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('patient_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = get_object_or_404(Patient, pk=self.kwargs['pk'])
        return context
    
class ScheduleAppointmentView(LoginRequiredMixin, View):
    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        procedures = Doctor.SPECIALTIES
        return render(request, 'patients/schedule_appointment.html', {
            'patient': patient,
            'procedures': procedures,
        })

    def post(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        procedure = request.POST.get('procedure')
        clinic_id = request.POST.get('clinic')
        doctor_id = request.POST.get('doctor')
        date_time = request.POST.get('date_time')

        clinic = get_object_or_404(Clinic, pk=clinic_id)
        doctor = get_object_or_404(Doctor, pk=doctor_id)

        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            clinic=clinic,
            date_time=date_time,
            procedure=procedure
        )

        return redirect('patient_detail', pk=pk)

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    visits = Visit.objects.filter(patient=patient)
    
    last_visit_info = visits.order_by('-date_time').first()
    
    next_appointment_info = Appointment.objects.filter(patient=patient).order_by('date_time').first()

    context = {
        'patient': patient,
        'visits': visits,
        'last_visit_info': last_visit_info,
        'next_appointment_info': next_appointment_info,
    }

    return render(request, 'patients/patient_detail.html', context)