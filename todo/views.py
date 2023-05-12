from django.shortcuts import render,redirect
from .models import Todo
from django.views import View

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, "index.html")

class AddTask(View):
    def post(self, request):
        newtodo = request.POST['task']
        date = request.POST['date']
        description = request.POST['description']
        todo = Todo(task=newtodo, date=date, description=description)
        todo.save()
        return redirect('/')

class ListTask(View):
    def get(self, request):
        todos = Todo.objects.all().order_by('-id')
        return render(request, "index.html", {'todos': todos, 'desc': False})

class DeleteTodo(View):
    def get(self,request, id):
        todo = Todo.objects.get(id = id)
        todo.delete()
        return redirect('/todos')
        
class UpdateTodo(View):
    def post(self, request, id,is_complete):
        newtodo = request.POST['task']
        date = request.POST['date']
        description = request.POST['description']
        todo = Todo.objects.get(id = id)
        todo.task = newtodo
        todo.date = date
        todo.description = description
        todo.save()
        return redirect('/')
    def get(self,request,id,is_complete):
        todo = Todo.objects.get(id = id)
        print(is_complete)
        todo.is_complete = bool(is_complete) 
        todo.save()
        return redirect('/todos')

class ShowTodo(View):
    def get(self, request,id):
        todo = Todo.objects.get(id = id)
        return render(request, "index.html", {'todo': todo, 'desc': True})
    