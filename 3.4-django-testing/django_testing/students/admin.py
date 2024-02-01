from django.contrib import admin

from students.models import Course, Student


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    pass


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    pass
