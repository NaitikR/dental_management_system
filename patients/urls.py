from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientListView.as_view(), name='patient_list'),
    path('<int:pk>/', views.PatientDetailView.as_view(), name='patient_detail'),
    path('create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient_update'),
    path('<int:pk>/add_visit/', views.VisitCreateView.as_view(), name='add_visit'),
    path('<int:pk>/schedule_appointment/', views.ScheduleAppointmentView.as_view(), name='schedule_appointment'),

]