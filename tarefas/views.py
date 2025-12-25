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
        
    
    form = TarefaForms
    return render(request, 'tarefas/adicionar.html', {'form': form})
    

def visualizar(request):
    lista = Tarefa.objects.all()
    return render(request, 'tarefas/visualizar.html', {'tarefas': lista})

def tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    return render(request, 'tarefas/tarefa.html', {'tarefa': tarefa})


def excluir(request):
    lista = Tarefa.objects.all()

    return render(request, 'tarefas/excluir.html', {'tarefas': lista})

def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)

    if request.method == 'POST':
        tarefa.delete()
        return redirect('home')
    
    return render(request, 'tarefas/excluir_tarefa.html', {'tarefa': tarefa})


def editar(request):
    lista = Tarefa.objects.all()

    return render(request, 'tarefas/editar.html', {'tarefas': lista})


def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)

    if request.method == 'POST':
        form = TarefaForms(request.POST, instance=tarefa)

        if form.is_valid():
            form.save()
            return redirect('home')
        
    form = TarefaForms(instance=tarefa)

    return render(request, 'tarefas/editar_tarefa.html', {'form': form})





