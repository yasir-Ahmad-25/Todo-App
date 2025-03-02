from django.urls import path
from .views import index,createTodo,updateTodo,deleteTodo

urlpatterns = [
    path('' , index , name="index"),
    path('create_todo' , createTodo , name="create-todo"),
    path('update_todo/<int:pk>' , updateTodo , name="update-todo"),
    path('delete_todo/<int:pk>' , deleteTodo , name="delete-todo"),
]