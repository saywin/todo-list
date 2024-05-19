from django.shortcuts import render
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

