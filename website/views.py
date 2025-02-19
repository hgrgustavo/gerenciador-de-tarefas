from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
from website import forms
from website.models import Usuario, Tarefa
from django.urls import reverse_lazy

class LayoutView(TemplateView):
    template_name = "layout.html"

class CadastroUsuario(CreateView):
    template_name = "cadastro_usuario.html"
    model = Usuario
    form_class = forms.CadastroUsuarioForm
    success_url = reverse_lazy("usuario_success_url")


class CadastroTarefa(CreateView):
    template_name = "cadastro_tarefa.html"
    model = Tarefa
    form_class = forms.CadastroTarefaForm
    success_url = reverse_lazy("tarefa_success_url")


class GerenciarTarefas(ListView):
    template_name = "gerenciar_tarefa.html"
    model = Tarefa
    context_object_name = "tarefas"

    

class SuccessUrl(TemplateView):
    template_name = "layout.html"


    