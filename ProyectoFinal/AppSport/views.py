from django.shortcuts import render
from django.http import HttpResponse

def inicio_view(request):
    return render(request, 'AppSport/inicio.html')

def socios_view(request):
    return render(request, 'AppSport/padre.html')

def actividades_view(request):
    return render(request, 'AppSport/padre.html')

def sedes_view(request):
    return render(request, 'AppSport/padre.html')
