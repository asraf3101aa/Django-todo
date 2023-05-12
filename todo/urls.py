from django.urls import path
from .views import IndexView,AddTask,DeleteTodo,ListTask,ShowTodo,UpdateTodo

from . import views
urlpatterns=[
    path('', IndexView.as_view(), name='index'),
    path('todo', AddTask.as_view()),
    path('todos', ListTask.as_view(),name='todos'),
    path('todo/<pk>/delete', DeleteTodo.as_view()),
    path('todo/<pk>/update', UpdateTodo.as_view()),
    path('todo/<pk>/update/<is_complete>', UpdateTodo.as_view()),
    path('todo/<pk>', ShowTodo.as_view()),
]