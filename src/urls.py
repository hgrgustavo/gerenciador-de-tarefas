from django.contrib import admin
from django.urls import path
from website import views


urlpatterns = [
    path('', views.LayoutView.as_view(), name="layout_view"),
    path('cadastro/usuario/', views.CadastroUsuario.as_view(), name="cadastro_usuario"),
    path('cadastro/tarefa/', views.CadastroTarefa.as_view(), name="cadastro_tarefa"),
    path('gerenciar/tarefa/', views.GerenciarTarefas.as_view(), name="gerenciar_tarefa"),
    path('cadastro/usuario/sucesso/', views.SuccessUrl.as_view(), name="usuario_success_url"),
    path('cadastro/tarefa/sucesso/', views.SuccessUrl.as_view(), name="tarefa_success_url"),
]
