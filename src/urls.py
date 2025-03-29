# from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.CreateUsuario.as_view(), name="createusuariopage"),
]
