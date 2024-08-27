from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Task
# Create your views here.

def index(request):
    return render(request, 'base.html')

#Listar tarefas
class tasksList(ListView):
    model = Task
    template_name = 'tasks/tasksList.html'

#Tarefas pendentes
def tasksPend(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, 'tasks/tasksPend.html', {'tasks': tasks})
#Tarefas completadas
def tasksComp(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'tasks/tasksComp.html', {'tasks': tasks})


#criar tarefas
class taskCreate(CreateView):
    model = Task    
    fields = ['title', 'description']
    template_name = 'form.html'
    success_url = '/'