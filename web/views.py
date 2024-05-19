
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from web.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "web/task_list.html"
    context_object_name = "task_list"
    paginate_by = 5

    class Meta:
        ordering = ["-deadline"]


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("web:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("web:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("web:task-list")


# @method_decorator(csrf_exempt, name="post")
class StatusTask(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("web:task-list")


class TagsListView(generic.ListView):
    model = Tag
    template_name = "web/tags_list.html"
    context_object_name = "tags_list"
    paginate_by = 5

    class Meta:
        ordering = ["name"]


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("web:tags-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("web:tags-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("web:tags-list")
