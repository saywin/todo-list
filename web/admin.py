from django.contrib import admin


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content", "datetime", "is_done", "deadline",
    )
    search_fields = ("content", )
    list_filter = ("is_done", "deadline",)
