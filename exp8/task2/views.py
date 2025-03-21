from django.shortcuts import render
from . import grades

def index(request):
    return render(request, 're.html')

def calc(request):
    if request.method == "POST":
        name = request.POST['Name']
        phy = float(request.POST['Phy'])
        chem = float(request.POST['Chem'])
        math = float(request.POST['Math'])

        marks = [phy, chem, math]

        std = grades.Student(name, marks)

        avg = std.calculate_average()
        avg_grd = std.assign_grade()

        return render(request, 're.html', {'name': name, 'marks': avg, 'grade': avg_grd})

