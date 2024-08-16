from django.contrib import admin

# Register your models here.

from .models import User, Habit

class HabitAdmin(admin.ModelAdmin):
    list_display = ("habit", "description", "status", "times_completed", "private")

admin.site.register(User)
admin.site.register(Habit, HabitAdmin)