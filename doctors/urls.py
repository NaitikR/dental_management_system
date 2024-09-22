from django.urls import path
from . import views
from .api import DoctorListCreateAPIView, DoctorDetailAPIView

urlpatterns = [
    path('', views.DoctorListView.as_view(), name='doctor_list'),
    path('<int:pk>/', views.DoctorDetailView.as_view(), name='doctor_detail'),
    path('create/', views.DoctorCreateView.as_view(), name='doctor_create'),
    path('<int:pk>/update/', views.DoctorUpdateView.as_view(), name='doctor_update'),
    path('api/doctors/', DoctorListCreateAPIView.as_view(), name='api_doctor_list'),
    path('api/doctors/<int:pk>/', DoctorDetailAPIView.as_view(), name='api_doctor_detail'),
]