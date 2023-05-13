from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.    
class TodoFunction():
    def index(self, request):
        return render(request, "index.html")
    
    def listTodo(self, request):
        todos = Todo.objects.all().order_by('-id')
        return render(request, "index.html", {'todos': todos, 'desc': False})   

    def addTodo(self, request):
        if request.method=='POST':
            newtodo = request.POST['task']
            date = request.POST['date']
            description = request.POST['description']
            todo = Todo(task=newtodo, date=date, description=description)
            todo.save()
            return redirect('/')
        
    def deleteTodo(self, request, id):
        todo = Todo.objects.get(id = id)
        todo.delete()
        return redirect('/todos')
    
    def updateTodo(self, request, id):
        if request.method=='POST':
            todo = Todo.objects.get(id = id)
            todo.task = request.POST['task']
            todo.date = request.POST['date']
            todo.description = request.POST['description']
            todo.save()
            return redirect('/todos')
        
    def updateStatus(self, request, id, is_complete):
        todo = Todo.objects.get(id = id)
        todo.is_complete = bool(is_complete) 
        todo.save()
        return redirect('/todos')
    
    def getTask(self, request, id):
        todo = Todo.objects.get(id = id)
        return render(request, "index.html", {'todo': todo, 'desc': True})


    '''

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
        '''


    