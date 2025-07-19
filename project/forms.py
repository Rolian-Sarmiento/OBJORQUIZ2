from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Portfolio, Project

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['portfolio_title', 'portfolio_description', 'projects']