from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio,  name='inicio'),
    path('home/', views.home, name='home'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('visualizar/', views.visualizar, name='visualizar'),
    path('tarefa/<int:id>/', views.tarefa, name='tarefa')
    
    
]
