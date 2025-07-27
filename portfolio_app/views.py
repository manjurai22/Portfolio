from django.shortcuts import render

# Create your views here.
from portfolio_app.models import Project
from protfolio_app.forms import ProjectForm

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

def project_create(request):
    if request.method == "GET":
        form = ProjectForm()
        return render(
            request,
            "project_create.html",
            {"form": form},
            )
    else:
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect("project-list")