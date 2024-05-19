from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from web.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "web/task_list.html"
    context_object_name = "task_list"

    class Meta:
        ordering = ["-deadline"]


class TagsListView(generic.ListView):
    model = Tag
    template_name = "web/tags_list.html"
    context_object_name = "tags_list"

    class Meta:
        ordering = ["name"]


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("web:task_list")

class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("web:task_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("web:task_list")


