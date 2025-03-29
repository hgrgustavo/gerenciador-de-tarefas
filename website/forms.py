from django import forms
from . import models


class CreateUsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = [
            "nome",
            "email"
        ]
        widgets = {
            "nome": forms.TextInput(attrs={"id": "nome__input", "class": "block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 px-20"}),
            "email": forms.EmailInput(attrs={"id": "email__input", "class": "block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 px-20"}),
        }


class CreateTarefaForm(forms.ModelForm):
    class Meta:
        model = models.Tarefa
        fields = [
            "usuario",
            "descricao",
            "setor",
            "prioridade",
            "data_cadastro",
            "status"
        ]
        widgets = {
            "descricao": forms.Textarea(attrs={"id": "desc__input", "rows": "3", "class": "block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"}),
            "setor": forms.EmailInput(attrs={"id": "setor__input", "class": "block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 px-23"}),
            "usuario": forms.Select(attrs={"id": "select", "class": "block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 px-42.5"}),
            "prioridade": forms.Select(attrs={"id": "select_1", "class": "block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 px-38"}),
        }

