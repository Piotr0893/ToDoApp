from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def Complete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.Status = True 
    task.save()
    return redirect('Task_List')	

def Not_Complete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.Status = False
    task.save()
    return redirect('Task_List')	


# Search for Task
def Search_Task(request):
    if request.method == "POST":
        searched = request.POST['searched']
        tasks = Task.objects.filter(Task_Name__contains = searched) # returns Tasks by name 
        return render(request, 'search_task.html', {'searched': searched, 'tasks': tasks})
    else:
         return render(request, 'search_task.html', {})

#Delete a Task
def Delete_Task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request, ("Your Task Has Been Deleted!")) 
    return redirect('Task_List')

#Update a Task
def Update_Task(request, task_id):
    task = Task.objects.get(pk=task_id)
    form = TaskForm(request.POST or None, instance = task)
    if form.is_valid():
        form.save()
        messages.success(request, ("Your Task Has Been Updated!")) 
        return redirect('Task_List')
    return render(request, 'update_task.html', {'task': task, "form": form })

#Add a Task 
def Add_Task(request):
    if request.method == "POST":                #if user is posting the form
        form = TaskForm(request.POST or None)   # pass request.Post into TaskForm (database)
        if form.is_valid():                     # if every box is filled up with correct data
            form.save()                         # then save it to database  
        messages.success(request, ("Your Task Has Been Submitted Successfully!"))           
        return redirect ('Task_List')
    else:
           form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def Task_Show(request, task_id):
    task= Task.objects.get(pk=task_id)
    return render(request, 'task_show.html', {"task": task})

def Task_List(request):
    task_list = Task.objects.all()
    return render(request, 'task.html', {"task_list": task_list})
    


