from django.urls import path
from django.http import HttpResponse


def inicio_view():
    return "Bienvenidos"

urlpatterns = [
    path('inicio/', inicio_view),
]
