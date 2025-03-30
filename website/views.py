from django.views.generic import edit, base, list
from . import models, forms
from django import http


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


class DeleteTarefa(edit.DeleteView):
    model = models.Tarefa

    def delete(self, request, **kwargs):
        try:
            self.get_object().delete()

            return http.JsonResponse({"status": "success"})

        except models.Tarefa.DoesNotExist:
            return http.JsonResponse({"status": "error", "cause": "Item not found"})
