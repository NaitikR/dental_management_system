from django.urls import path
from .api import ClinicListCreateAPIView, ClinicDetailAPIView
from . import views

urlpatterns = [
    path('', views.ClinicListView.as_view(), name='clinic_list'),
    path('<int:pk>/', views.ClinicDetailView.as_view(), name='clinic_detail'),
    path('create/', views.ClinicCreateView.as_view(), name='clinic_create'),
    path('<int:pk>/update/', views.ClinicUpdateView.as_view(), name='clinic_update'),
    path('<int:pk>/add_doctor/', views.DoctorAffiliationCreateView.as_view(), name='add_doctor_affiliation'),
]