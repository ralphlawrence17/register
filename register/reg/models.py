from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    SEX = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    id_no = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    birth_date = models.DateTimeField(auto_now_add=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(
        max_length=10, choices=SEX, blank=True, null=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}"


class Subject(models.Model):
    subject_code = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=255, unique=True)
    units = models.IntegerField()
    students = models.ForeignKey(
        Student, related_name="student", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject_code} - {self.title}"
    
class Position(models.Model):
    position_name = models.TextField(max_length=20)
    note = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.position_name}"

class Teacher(models.Model):
    id_no = models.CharField(max_length=10, unique=True, db_index=True)
    last_name = models.TextField(max_length=40)
    first_name = models.TextField(max_length=40)
    middle_name =  models.TextField(max_length=20)
    position = models.ForeignKey(
        Position, related_name="position", on_delete=models.CASCADE)
    salary = models.FloatField(max_length=6)
    date_hired = models.DateTimeField(auto_now_add=False)


    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}"
    
