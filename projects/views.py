from django.shortcuts import render
from .models import Projects


def Projectindex(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projectindex.html', context)


def Projectdetail(request, pk):
    projects = Projects.objects.get(pk=pk)
    context = {
        'projects': projects
    }
    return render(request, 'projectdetail.html', context)
