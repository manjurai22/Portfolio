from django.shortcuts import render

# Create your views here.
from portfolio_app.models import Project

def portfolio(request):
    projects=Project.objects.all()
    return render(
        request,
        "project_list.html",
        {"projects":projects}
    )

def project_list(request):
    projects = Project.objects.all()
    return render(
        request,
        'project_list.html',
        {'projects': projects}
    )