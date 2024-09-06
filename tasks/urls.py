from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views

app_name = "tasks"
urlpatterns = [
    path('', views.index, name='index'),   
    path('tasks/tasksList', views.tasksList.as_view(), name='lista'),
    path('tasks/pendentes/', views.tasksPend, name='pendentes'),
    path('tasks/completadas/', views.tasksComp, name='completadas'),
    path('tasks/taskCreate/', views.tasksCreate.as_view(), name='novo'),   
    path('tasks/<int:pk>/taskDelete',views.tasksDelete.as_view(), name='excluir'),
    path('tasks/<int:pk>/taskupdate',views.tasksUpdate.as_view(), name='editar'),
    

    # URLs de autenticação
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html', next_page='tasks:index'), name='logout'),   
]