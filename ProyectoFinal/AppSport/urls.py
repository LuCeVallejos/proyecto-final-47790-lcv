from django.urls import path
from AppSport.views import inicio_view, crearsocio_view, socio_buscar_view

# actividades_view, sedes_view, socios_view

#urlpatterns = [
#    path('inicio/', inicio_view, name="inicio"),
#    path('socios/', socios_view),    
#    path('actividades/', actividades_view),
#    path('sedes/', sedes_view),
#]


urlpatterns = [
    path("", inicio_view, name="inicio"),
    path("socio/crear/", crearsocio_view, name="crear-socio"),
    path("socio/buscar", socio_buscar_view, name="buscar-socio"),
]