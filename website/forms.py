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
            "nome": forms.TextInput(attrs={"id": "nome__input", "class": "block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"}),
            "email": forms.EmailInput(attrs={"id": "email__input", "class": "block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"}),
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
        ]
        widgets = {
            "descricao": forms.Textarea(attrs={"id": "desc__input", "rows": "3", "class": "block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"}),
            "setor": forms.TextInput(attrs={"id": "setor__input", "class": "block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 px-23"}),
            "usuario": forms.Select(attrs={"id": "usuario__select", "class": "block w-full rounded-md bg-white py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm grow-0 overflow-hidden text-ellipsis px-27.5"}),
            "prioridade": forms.Select(attrs={"id": "prioridade__select", "class": "block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 px-37.5"}),
            "data_cadastro": forms.DateInput(attrs={"id": "data_nascimento", "type": "date", "class": "block w-full rounded-md bg-white px-3 py-1.5 text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 px-29.5"}),
        }


class UpdateTarefaStatusForm(forms.ModelForm):
    class Meta:
        model = models.Tarefa
        fields = ["status"]
        widgets = {
            "status": forms.Select(attrs={"id": "status__select", "class": "block w-full rounded-md bg-white py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm grow-0 overflow-hidden text-ellipsis px-3"}),
        }
