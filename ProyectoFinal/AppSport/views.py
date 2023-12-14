from django.shortcuts import render
from .forms import SocioBuscarFormulario, SocioFormulario
from .models import Socio
#from django import redirectttpResponse

def inicio_view(request):
    return render(request, 'AppSport/inicio.html')

def socio_view(request):
    return render(request, 'AppSport/padre.html')

#def actividad_view(request):
#    return render(request, 'AppSport/padre.html')

#def sede_view(request):
    return render(request, 'AppSport/padre.html')

def crearsocio_view(request):
    if request.method == "GET":
        # mostrar formulario
        contexto = {'form':SocioFormulario()}
        return render(request, 'AppSport/formulario_avanzado_socio.html', context = contexto)
    else:
        # procesar formulario
        print (request.POST)
        formulario=SocioFormulario(request.POST)
        if formulario.is_valid():
            informacion_limpia=formulario.cleaned_data
            modelo = Socio(
                dni=informacion_limpia['dni'],
                nombre=informacion_limpia['nombre'],
                apellido=informacion_limpia['apellido'],
                nacimiento=informacion_limpia['nacimiento'],
                )
            modelo.save()
            return render(request, 'AppSport/inicio.html')



def socio_buscar_view(request):
    if request.method == "GET":
        form = SocioBuscarFormulario()
        return render(request, 'AppSport/formulario_avanzado_socio.html', context={"form": form})
    else:
        formulario = SocioBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            socios_filtrados = []
            for dni in Socio.objects.filter(dni=informacion["dni"]):
                socios_filtrados.append(dni)
            contexto = {"dni": socios_filtrados}
            return render(request, "AppSport/socios_list.html", context=contexto)