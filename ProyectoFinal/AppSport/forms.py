from django import forms

class SocioFormulario(forms.Form):
    dni = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    nacimiento = forms.DateField()


class SocioBuscarFormulario(forms.Form):
    dni = forms.CharField(max_length=100)