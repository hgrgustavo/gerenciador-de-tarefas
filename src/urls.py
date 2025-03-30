# from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.Index.as_view(), name="indexpage"),
    path(
        "cadastro/",
        include([
            path("usuario/", views.CreateUsuario.as_view(),
                 name="createusuariopage"),
            path("tarefa/", views.CreateTarefa.as_view(),
                 name="createtarefapage"),

        ])
    ),
    path("gerenciar/",
         include([
             path("tarefas/", views.ListTarefa.as_view(),
                 name="listtarefapage"),

             path("tarefas/editar-tarefa/<int:pk>/",
                  views.UpdateTarefa.as_view(), name="updatetarefapage"),

             path("tarefas/atualizar-status/<int:pk>/",
                  views.UpdateTarefaStatus.as_view(), name="updatestatuspage"),

             path("tarefas/excluir/<int:pk>/",
                  views.DeleteTarefa.as_view(), name="deletetarefapage"),
         ]),
         name="gerenciartarefapage"),
]
