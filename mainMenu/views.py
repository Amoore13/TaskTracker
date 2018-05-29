from django.shortcuts import render
from task.models import Task


def index(request):
    return render(request, 'mainMenu/index.html', locals())


def tasks(request):
    """Выводит список задач."""
    tasks = Task.objects.order_by('name')
    context = {'tasks': tasks}
    return render(request, 'mainMenu/tasks.html', context)


def task(request, task_id):
    """Вьюха для одной задачи."""
    task = Task.objects.get(id=task_id)
    entries = task.entry_set.order_by('-text')
    context = {'task': task, 'entries': entries}
    return render(request, 'mainMenu/task.html', context)
