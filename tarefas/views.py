from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForms
from .models import Tarefa

# Create your views here.

def inicio(request):

    if request.method == "POST":
        request.session["nome"] = request.POST.get("nome")
        return redirect("home")
    return render(request, 'tarefas/inicio.html')

def home(request):
    nome = request.session.get("nome")

    if not nome:
        return redirect("inicio")
    
    return render(request, 'tarefas/home.html', {'nome': nome})


def adicionar(request):
    nome = request.session.get("nome")

    if request.method == "POST":
        form = TarefaForms(request.POST)
        
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.criado_por = nome
            tarefa.save()
            return redirect("home")
        
    else:
        form = TarefaForms
        return render(request, 'tarefas/adicionar.html', {'form': form})
    

def visualizar(request):
    lista = Tarefa.objects.all()
    return render(request, 'tarefas/visualizar.html', {'tarefas': lista})

def tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    return render(request, 'tarefas/tarefa.html', {'tarefa': tarefa})


