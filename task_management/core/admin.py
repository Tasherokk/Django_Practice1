from django.contrib import admin

from .models import Task, Priority, Category, Project, User


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = []