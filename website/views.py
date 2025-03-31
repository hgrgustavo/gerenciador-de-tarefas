from django.views.generic import edit, base, list
from . import models, forms
from django import http
import json
from django.urls import reverse_lazy


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

        return context


class UpdateTarefaStatus(edit.UpdateView):
    model = models.Tarefa

    def post(self, request, **kwargs):
        try:
            new_status = json.loads(request.body).get("status")

            if new_status not in [key for key, _ in models.Tarefa.CHOICES_STATUS]:
                return http.JsonResponse({"success": False, "cause": "Invalid status"}, status=400)

            task = self.get_object()
            task.status = new_status
            task.save()

            return http.JsonResponse({"success": True})

        except models.Tarefa.DoesNotExist:
            return http.JsonResponse({"success": False, "cause": "Item not found"}, status=404)


class DeleteTarefa(edit.DeleteView):
    model = models.Tarefa

    def delete(self, request, **kwargs):
        try:
            self.get_object().delete()

            return http.JsonResponse({"status": "success"})

        except models.Tarefa.DoesNotExist:
            return http.JsonResponse({"status": "error", "cause": "Item not found"})


class UpdateTarefa(edit.UpdateView):
    model = models.Tarefa
    template_name = "update_tarefa.html"
    form_class = forms.UpdateTarefa
    success_url = "updatetarefapage"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_pk"] = self.get_object().id

        return context
