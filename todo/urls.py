from django.urls import path
from .views import index,createTodo

urlpatterns = [
    path('' , index , name="index"),
    path('create_todo' , createTodo , name="create-todo")
]