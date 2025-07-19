from django.shortcuts import render
from.settings import DEBUG


def list_view(request):
    return render(request, "list.html")

def detailed_view(request):
    return render(request, "detailed.html")