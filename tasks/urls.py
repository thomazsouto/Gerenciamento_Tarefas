from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path('', views.index, name='list'),
    path('tasks/tasksList', views.tasksList.as_view(), name='list'),
    path('tasks/taskCreate', views.taskCreate.as_view(), name='novaTarefa'),
]