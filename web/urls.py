from django.urls import path

from web.views import (
    TaskListView,
    TaskCreateView,
    TagsListView, TaskUpdateView, TaskDeleteView,
)

urlpatterns = [
    path("todo-list/", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
]

app_name = "web"
