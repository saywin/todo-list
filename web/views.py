from django.shortcuts import render
from django.views import generic

from web.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "web/task_list.html"
    context_object_name = "task_list"

    class Meta:
        ordering = ["-deadline"]
