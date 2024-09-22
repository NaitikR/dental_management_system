from django.contrib import admin
from .models import Clinic, DoctorAffiliation

# Register your models here.

admin.site.register(Clinic)
admin.site.register(DoctorAffiliation)