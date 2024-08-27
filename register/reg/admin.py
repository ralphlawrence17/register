from django.contrib import admin
from .models import Student, Subject, Teacher, Position

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Position)
