from django.views.generic import edit, base, list
from . import models, forms


class Index(base.TemplateView):
    template_name = "index.html"


class CreateUsuario(edit.CreateView):
    template_name = "create_usuario.html"
    model = models.Usuario
    form_class = forms.CreateUsuarioForm
    success_url = "#"


class CreateTarefa(edit.CreateView):
    template_name = "create_tarefa.html"
    model = models.Tarefa
    form_class = forms.CreateTarefaForm
    success_url = "#"


class ListTarefa(list.ListView):
    template_name = "list_tarefa.html"
    model = models.Tarefa
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = forms.UpdateTarefaStatusForm

        return context


class UpdateTarefaStatus(edit.UpdateView):
    template_name = "list_tarefa.html"
    model = models.Tarefa
    form_class = forms.UpdateTarefaStatusForm
    success_url = "#"
