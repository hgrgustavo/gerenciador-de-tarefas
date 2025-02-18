from django.forms import ModelForm, TextInput, Select
from website.models import Tarefa, Usuario

class CadastroUsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

    class Meta:
        model = Usuario
        fields = [
            "nome",
            "email"
        ]
        widgets = {
            "nome": TextInput(attrs={"placeholder": "Nome", "required": "required"}),
            "email": TextInput(attrs={"placeholder": "Email", "required": "required"})
        }

class CadastroTarefaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].choices = [(user.id, user.nome) for user in Usuario.objects.all()]

      
    class Meta:
        model = Tarefa
        fields = [
            "setor",
            "prioridade",
            "usuario",
            "descricao",
            "usuario"
        ]
        widgets = {
            "descricao": TextInput(attrs={"placeholder": "Descrição", "required": "required"}),
            "setor": TextInput(attrs={"placeholder": "Setor", "required": "required"}),
        }