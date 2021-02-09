from django.shortcuts import render, HttpResponse
from .models import Project


# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request,"core/home.html",{'projects':projects})


def about(request):
    return render(request,"core/about.html")


def portfolio(request):
    return render(request, "core/portfolio.html")

def contacto(request):
    return render(request, "core/contacto.html")