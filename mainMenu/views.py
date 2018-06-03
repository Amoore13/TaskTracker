from django.shortcuts import render
from task.models import Task
from task.forms import TaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse


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


def new_task(request):
    """Определяет новую задачу."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TaskForm()

    else:
        # Отправлены данные POST; обработать данные.
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainMenu:tasks'))
    context = {'form': form}
    return render(request, 'mainMenu/new_task.html', context)


def edit_task(request, task_id):
    """Редактирует существующую запись."""
    task = Task.objects.get(id=task_id)
    #topic = entry.topic

    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = TaskForm(instance=task)
    else:
        # Отправка данных POST; обработать данные.
        form = TaskForm(instance=task, data=request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('mainMenu:task',
                                        args=[task.id]))

    context = {'task': task(), 'form': form}
    return render(request, 'mainMenu/edit_task.html', context)