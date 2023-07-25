from django import forms
from .models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model= Contacto
        fields= ["id",'nombre_apellido','email','asunto','mensaje','fecha' ]

    