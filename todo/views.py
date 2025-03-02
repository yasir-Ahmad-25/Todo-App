from django.shortcuts import render,redirect,get_object_or_404

from .models import Tasks
from .forms import TodoForm
# Create your views here.
def index(request):
    todos = Tasks.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, 'todo/todo_list.html' , context)

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
 

# update Task Form
def updateTodo(request,pk):
    # if request.user.is_authenticated:
    object = get_object_or_404(Tasks , pk=pk)
    if request.method == "POST":
        form  = TodoForm(request.POST , instance=object)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('index')
    else:
        context = {
            'form' : TodoForm(instance=object)
        }
    return render(request , 'todo/update_task.html' , context)


# delete Task Form
def deleteTodo(request,pk):
    todo = get_object_or_404(Tasks , pk=pk)
    todo.delete()
    return redirect('index')