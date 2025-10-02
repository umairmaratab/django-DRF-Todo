from django.contrib import admin

# Register your models here.
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body"
    )
    search_fields = ("title",)

admin.site.register(Todo, TodoAdmin)
