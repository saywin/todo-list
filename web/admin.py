from django.contrib import admin

from web.models import Task, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content", "datetime", "is_done", "deadline",
    )
    search_fields = ("content", )
    list_filter = ("is_done", "deadline",)
