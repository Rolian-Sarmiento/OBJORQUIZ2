from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_title = models.CharField(max_length=100)
    portfolio_description = models.TextField()
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return f"{self.user.first_name} - Portfolio"