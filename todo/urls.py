from django.urls import path
from todo import views
urlpatterns=[
    path('', views.TodoFunction().index, name='index'),
    path('todo', views.TodoFunction().addTodo),
    path('todos', views.TodoFunction().listTodo,name='todos'),
    path('todo/<int:id>/delete', views.TodoFunction().deleteTodo),
    path('todo/<int:id>/update', views.TodoFunction().updateTodo),
    path('todo/<int:id>/update/<int:is_complete>', views.TodoFunction().updateStatus),
    path('todo/<int:id>', views.TodoFunction().getTask),


    # '''
    # path('todo/<int:id>/<str:function>', views.TodoFunction.as_view()),
    # path('todo/<int:id>/<str:function>', TodoFunction.as_view()),
    # path('todo/<int:id>/<str:function>/<int:is_complete>', TodoFunction.as_view()),
    # '''
]