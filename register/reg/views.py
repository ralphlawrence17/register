from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



from .models import Student, Subject, Teacher, Position
from .forms import StudentForm, SubjectForm, TeacherForm, PositionForm



def logout_view(request):
    logout(request)
    return redirect('login')





def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('students')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('students')
        else:
            error_message = 'Invalid credentials'
    else:
        error_message = ''
    return render(request, 'login.html', {'error_message': error_message})


@login_required
def stud_list(request):
    query = request.GET.get('search', '')
    if query:
        students = Student.objects.filter(
            Q(last_name__icontains=query) |
            Q(first_name__icontains=query)  # , user=request.user
        )
    else:
        # students = Student.objects.filter(user=request.user)#
        students = Student.objects.all()

    return render(request, 'students/students.html', {'students': students, 'query': query})


@ login_required
def stud_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            stud = form.save(commit=False)
            stud.user = request.user
            stud.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})


def stud_update(request, pk):
    todo = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=todo)
    return render(request, 'students/student_form.html', {'form': form})


def stud_delete(request, pk):
    stud = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        stud.delete()
        return redirect('students')
    return render(request, 'students/student_confirm_delete.html', {'stud': stud})




@login_required
def sub_list(request):
    query = request.GET.get('search', '')
    if query:
        subjects = Subject.objects.filter(
            Q(subject_code__icontains=query) |
            Q(title__icontains=query)  # , user=request.user
        )
    else:
        # students = Student.objects.filter(user=request.user)#
        subjects = Subject.objects.all()

    return render(request, 'subjects/subjects.html', {'subjects': subjects, 'query': query})

@ login_required
def sub_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subs = form.save(commit=False)
            subs.user = request.user
            subs.save()
            return redirect('subjects')
    else:
        form = SubjectForm()
    return render(request, 'subjects/subject_form.html', {'form': form})

def sub_update(request, pk):
    sub = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=sub)
        if form.is_valid():
            form.save()
            return redirect('subjects')
    else:
        form = SubjectForm(instance=sub)
    return render(request, 'subjects/subject_form.html', {'form': form})

def sub_delete(request, pk):
    sub = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        sub.delete()
        return redirect('subjects')
    return render(request, 'subjects/subject_confirm_delete.html', {'sub': sub})




@login_required
def teacher_list(request):
    query = request.GET.get('search', '')
    if query:
        teachers = Teacher.objects.filter(
            Q(first_name__icontains=query) |
            Q(position__icontains=query)  # , user=request.user
        )
    else:
        # students = Student.objects.filter(user=request.user)#
        teachers = Teacher.objects.all()

    return render(request, 'teachers/teachers.html', {'teachers': teachers, 'query': query})

@ login_required
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = request.user
            teacher.save()
            return redirect('teachers')
    else:
        form = TeacherForm()
    return render(request, 'teachers/teachers_form.html', {'form': form})


def teacher_update(request, pk):
    teach = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teach)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form = TeacherForm(instance=teach)
    return render(request, 'teachers/teachers_form.html', {'form': form})

def teacher_delete(request, pk):
    teach = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teach.delete()
        return redirect('teachers')
    return render(request, 'teachers/teachers_confirm_delete.html', {'teach': teach})




@login_required
def position_list(request):
    query = request.GET.get('search', '')
    if query:
        positions = Position.objects.filter(
            Q(first_name__icontains=query) |
            Q(position__icontains=query)  # , user=request.user
        )
    else:
        # students = Student.objects.filter(user=request.user)#
        positions = Position.objects.all()

    return render(request, 'position/positions.html', {'positions': positions, 'query': query})

@ login_required
def add_position(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            position = form.save(commit=False)
            position.user = request.user
            position.save()
            return redirect('positions')
    else:
        form = PositionForm()
    return render(request, 'position/position_form.html', {'form': form})


def update_position(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('positions')
    else:
        form = PositionForm(instance=position)
    return render(request, 'position/position_form.html', {'form': form})

def delete_position(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        position.delete()
        return redirect('positions')
    return render(request, 'position/position_confirm_delete.html', {'position': position})