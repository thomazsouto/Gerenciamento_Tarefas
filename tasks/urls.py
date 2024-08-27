from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/tasksList', views.tasksList.as_view(), name='tasks_list'),
    path('tasks/pendentes/', views.tasksPend, name='pendentes'),
    path('tasks/completadas/', views.tasksComp, name='completadas'),
   #path('tasks/taskCreate', views.taskCreate.as_view(), name='novaTarefa'),
]