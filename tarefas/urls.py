from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio,  name='inicio'),
    path('home/', views.home, name='home'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('visualizar/', views.visualizar, name='visualizar'),
    path('tarefa/<int:id>/', views.tarefa, name='tarefa'),
    path('excluir/', views.excluir, name='excluir'),
    path('tarefa/excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('editar/', views.editar, name='editar'),
    path('tarefa/editar/<int:id>/', views.editar_tarefa, name='editar_tarefa')
]
