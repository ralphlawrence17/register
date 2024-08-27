from django import forms
from .models import Student, Subject, Teacher, Position


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id_no', 'last_name', 'first_name',
                  'middle_name', 'gender', 'address', 'birth_date']
        widgets = {
            'id_no': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'id number'}),
            'last_name': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'first_name': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'birth_date': forms.DateInput
            (attrs={'class': 'form-control', 'type': 'date'}),
        }



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_code', 'title', 'units', 'students']
        widgets = {
            'subject_code': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'Subject code'}),
            'title': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'units': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'Units'}),
            'students': forms.Select
            (attrs={'class': 'form-control', 'placeholder': 'Students'}),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['id_no', 'last_name', 'first_name', 'middle_name', 'position',
                    'salary', 'date_hired']
        widgets = {
            'id_no': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'ID no.'}),
            'last_name': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'first_name': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'middle_name': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'position': forms.Select
            (attrs={'class': 'form-control', 'placeholder': 'Position'}),
            'salary': forms.NumberInput
            (attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'date_hired': forms.DateInput
            (attrs={'class': 'form-control', 'type': 'date'}),
        }

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['position_name', 'note']
        widgets = {
            'position_name': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'Position Name'}),
            'note': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'Position'}),
        }