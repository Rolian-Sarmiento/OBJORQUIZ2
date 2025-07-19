# portfolio/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Portfolio, Project

def applicant_list(request):
    applications = User.objects.select_related('user').all()
    context = {
        'applications': applications,
        'position': 'Junior Developer'
    }
    return render(request, 'list.html', context)

class ApplicantDetailView(DetailView):
    model = User
    template_name = 'detailed.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'applicant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio'] = Portfolio.objects.filter(user=self.object).first()
        return context

class ApplicantDeleteView(DeleteView):
    model = User
    template_name = 'delete.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    success_url = reverse_lazy('applicant_list')