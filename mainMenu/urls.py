"""youTrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from mainMenu import views

urlpatterns = [
    url(r'^mainMenu/', views.index, name='index'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^tasks/(?P<task_id>\d+)/$', views.task, name='task'),
    url(r'^new_task/$', views.new_task, name='new_task'),
    url(r'^add_comment/$', views.add_comment, name='add_comment'),
    url(r'^edit_task/(?P<task_id>\d+)/$', views.edit_task, name='edit_task'),
]
