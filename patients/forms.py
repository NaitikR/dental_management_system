from django import forms
from .models import Appointment
from doctors.models import Doctor

class AppointmentForm(forms.ModelForm):
    procedure = forms.ChoiceField(
        choices=Doctor.SPECIALTIES,
        widget=forms.Select
    )

    class Meta:
        model = Appointment
        fields = ['procedure', 'clinic', 'doctor', 'date_time']