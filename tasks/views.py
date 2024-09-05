from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'base.html')

#Listar tarefas
class tasksList(LoginRequiredMixin ,ListView):
    model = Task
    template_name = 'tasks/tasksList.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)  # Filtra tarefas associadas ao usuário logado

#Tarefas pendentes
@login_required
def tasksPend(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, 'tasks/tasksPend.html', {'tasks': tasks})
#Tarefas completadas
@login_required
def tasksComp(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'tasks/tasksComp.html', {'tasks': tasks})


#Criar tarefa
class tasksCreate(LoginRequiredMixin, CreateView):
    model = Task    
    fields = ['title', 'description', 'user','due_date']
    template_name = 'tasks/taskInsert.html'
    success_url = '/'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['due_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        return form

#Alterar tarefa

class tasksUpdate(LoginRequiredMixin, UpdateView):
    model = Task    
    fields = ['title', 'description', 'user','due_date']
    template_name = 'tasks/tasksUpdate.html'
    success_url = '/'

class tasksDelete(LoginRequiredMixin, DeleteView):
    model = Task    
    fields = ['title', 'description', 'user','due_date']
    template_name = 'tasks/tasksDelete.html'
    success_url = '/'
