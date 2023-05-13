from django.shortcuts import render,redirect
from .models import Todo
from django.views import View

# Create your views here.    
class TodoFunction(View):
    def get(self, request, **kwargs):
        if not kwargs:
            return render(request, "index.html")
        
        #Lists all tasks
        if kwargs.get('base')=='todos':
            todos = Todo.objects.all().order_by('-id')
            return render(request, "index.html", {'todos': todos, 'desc': False})   
         
        #Lists a todo with description according to id
        if kwargs.get('id') is not None and kwargs.get('function') is None:
            todo = Todo.objects.get(id = kwargs.get('id'))
            return render(request, "index.html", {'todo': todo, 'desc': True})
        
        #Update complete status
        if kwargs.get('function')=='update' and kwargs.get('is_complete') is not None:
            todo = Todo.objects.get(id = kwargs.get('id'))
            todo.is_complete = bool(kwargs.get('is_complete')) 
            todo.save()
            return redirect('/todos')
        
        #Delete a Todo
        if kwargs.get('function')=='delete':
            todo = Todo.objects.get(id = kwargs.get('id'))
            todo.delete()
            return redirect('/todos')
    
    def post(self,request,**kwargs):
        #Add a Todo
        if kwargs.get('base')=='todo':
            newtodo = request.POST['task']
            date = request.POST['date']
            description = request.POST['description']
            todo = Todo(task=newtodo, date=date, description=description)
            todo.save()
            return redirect('/')
        
        #Update a todo
        if kwargs.get('function')=='update':
            todo = Todo.objects.get(id = kwargs.get('id'))
            todo.task = request.POST['task']
            todo.date = request.POST['date']
            todo.description = request.POST['description']
            todo.save()
            return redirect('/todos')


    