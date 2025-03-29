from django import forms 
from . import models 


class CreateUsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario 
        fields = ["nome", "email"] 
        widegts = {}