from django.urls import path

from web.views import (
    TaskListView,
    TaskCreateView,
    TagsListView,
    TaskUpdateView,
    TaskDeleteView,
    StatusTask,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("todo-list/", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("status/<int:pk>/", StatusTask.as_view(), name="task-status"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "web"
