from django.urls import path
from AppSport.views import inicio_view, actividades_view, sedes_view, socios_view

urlpatterns = [
    path('inicio/', inicio_view),
    path('socios/', socios_view),    
    path('actividades/', actividades_view),
    path('sedes/', sedes_view),
]
