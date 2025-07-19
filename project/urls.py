# portfolio/urls.py
from django.urls import path
from .views import applicant_list, ApplicantDetailView, ApplicantDeleteView


urlpatterns = [
    path('', applicant_list, name='applicant_list'),
    path('portfolio/<str:username>/', ApplicantDetailView.as_view(), name='applicant_detail'),
    path('delete/<str:username>/', ApplicantDeleteView.as_view(), name='applicant_delete'),
]