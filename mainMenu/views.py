from django.shortcuts import render
from task.models import Task
from task.forms import TaskForm
from task.forms import CommentForm
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
    comments = task.comment_set.order_by('-date_added')
    context = {'task': task, 'comments': comments}
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

    context = {'task': task, 'form': form}
    return render(request, 'mainMenu/edit_task.html', context)


def add_comment(request):
    """Добавляем комментарий"""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = CommentForm()

    else:
        # Отправлены данные POST; обработать данные.
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainMenu:task',
                                                args=[task.id]))
    context = {'form': form}
    return render(request, 'mainMenu/add_comment.html', context)
