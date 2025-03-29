from django.views.generic import edit
from . import models, forms

class CreateUsuario(edit.CreateView):
    template_name = "create_usuario.html"
    model = models.Usuario 
    form_class = forms.CreateUsuarioForm
    success_url = "#"