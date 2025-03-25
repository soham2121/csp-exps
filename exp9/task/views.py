from django.shortcuts import render, redirect
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        app_id = request.POST['app_id']
        name = request.POST['name']
        marks = request.POST['marks']
        Student.objects.create(app_id=app_id, name=name, marks=marks)
        return redirect('index')