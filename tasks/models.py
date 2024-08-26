from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    # A data e hora da criação da tarefa ela é definida quando criada a tarefa.
    created_at = models.DateTimeField(auto_now_add=True)
    #Data e hora prevista para finalização da tarefa.
    due_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
