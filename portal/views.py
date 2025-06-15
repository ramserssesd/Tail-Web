from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

@login_required
def add_or_update_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        marks = int(request.POST['marks'])

        if request.POST['studentid']:
            student = Student.objects.filter(id=request.POST['studentid']).update(name=name, subject=subject, marks=marks)
            messages.success(request, "Student updated successfully.")
        else:
            Student.objects.create(name=name, subject=subject, marks=marks)
            messages.success(request, "Student created successfully.")
    return redirect('home')

@login_required
def delete_student(request, id):
    Student.objects.get(id=id).delete()
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('login')

