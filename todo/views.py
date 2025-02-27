from django.shortcuts import render,redirect

from .models import Tasks
from .forms import TodoForm
# Create your views here.
def index(request):
    return render(request, 'todo/todo_list.html' , {})

# create Task Form
def createTodo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
        context = {
            'form' : form
        }
        return render(request , 'todo/create_task.html', context)
