from django.contrib import admin
from . models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date', 'priority', 'created_at']
    search_fields = ['title']
    list_filter = ['completed', 'priority']