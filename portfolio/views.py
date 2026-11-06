from django.shortcuts import render
#from django.http import HttpResponse
from .models import Project

def fx_home(request):
    t_projects = Project.objects.all()
    return render(request, "portfolio/home.html", {'key_projects':t_projects})
