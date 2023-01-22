from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy #just redirects user to certain page in app
from .models import Task

# Create your views here.
#request -> response
#request handler
#action


class TaskList(ListView):
    model = Task 
    context_object_name = 'tasks'
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(CreateView): #inherit from create view , seding a post request but create a item
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
    

    