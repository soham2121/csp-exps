from django.shortcuts import render
from . import rectangle

def index(request):
    return render(request, 'index.html')

def calculate_area(request):
    if request.method == "POST":
        length = float(request.POST['Length'])
        width = float(request.POST['Width'])

        rect = rectangle.Reactangle(length, width)
        result = rect.area()

        return render(request, 'index.html', {'area': result})