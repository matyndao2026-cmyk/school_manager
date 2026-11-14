from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "classe", "email", "phone", "active")
    list_filter = ("classe", "active")
    search_fields = ("last_name", "first_name", "email")