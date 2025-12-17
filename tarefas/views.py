from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'tarefas/inicio.html')

def home(request):
    return render(request, 'tarefas/home.html')
