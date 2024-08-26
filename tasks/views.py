from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Task
# Create your views here.

def index(request):
    return render(request, 'index.html')

#Listar tarefas
class tasksList(ListView):
    model = Task
    tamplate_name = 'task_list.html'

#criar tarefas
class taskCreate(CreateView):
    model = Task    
    fields = ['title', 'description']
    template_name = 'form.html'
    success_url = '/'