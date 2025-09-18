from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'webapp/task_list.html', {'tasks': tasks})
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'webapp/add_task.html')