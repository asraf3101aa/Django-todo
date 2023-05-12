from django.shortcuts import render,redirect
from .models import Todo
from django.views.generic import CreateView,ListView, DeleteView, TemplateView, DetailView, UpdateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class AddTask(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'index.html'
    success_url = '/'

class ListTask(ListView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'todos'
    ordering = ['-id']
    extra_context = {'desc': False}

class DeleteTodo(DeleteView):
    model = Todo
    success_url = ('/todos')

    
    #skip confirm template
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
class UpdateTodo(UpdateView):
    model = Todo
    fields = ['task','description','date']
    template_name = 'index.html'
    success_url = '/'
    

    
     

class ShowTodo(DetailView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'todo'
    extra_context = {'desc': True}
    