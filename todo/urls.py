from django.urls import path
from .views import TodoFunction

from . import views
urlpatterns=[
    path('', TodoFunction.as_view(), name='index'),
    path('<str:base>', TodoFunction.as_view()),
    path('<str:base>', TodoFunction.as_view(),name='todos'),
    path('todo/<int:id>/<str:function>', TodoFunction.as_view()),
    path('todo/<int:id>/<str:function>', TodoFunction.as_view()),
    path('todo/<int:id>/<str:function>/<int:is_complete>', TodoFunction.as_view()),
    path('todo/<int:id>', TodoFunction.as_view()),
]