from django.shortcuts import render
from .forms import TaskForm


# def landing(request):
#     name = "Dmitryk"
#     form = TaskForm(request.POST or None)
#
#     if request.method == "POST":
#         print(form)
#
#         form_new = form.save()
#
#     return render(request, 'landing/landing.html', locals())
