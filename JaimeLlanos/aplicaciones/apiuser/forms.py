from dataclasses import field
from pyexpat import model
from django import forms
from .models import Jaime
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Jaime
        fields ='__all__'

        widgets = {
           'nombre': forms.TextInput(attrs={'class':'input'}) ,
           'apellido': forms.TextInput(attrs={'class':'input'}) ,
           'edad': forms.TextInput(attrs={'class':'input'}) ,
           'sexo': forms.Select(attrs={'class':'input-select'}) ,
           'telefono': forms.TextInput(attrs={'class':'input'}) ,
           'direccion': forms.TextInput(attrs={'class':'input'}) ,
        }