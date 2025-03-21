from django.shortcuts import render
from grades import Student

def index(request):
    return render(request, 're.html')

def calc(request):
    if request.method == "POST":
        name = float(request.POST['Name'])
        phy = float(request.POST['Phy'])
        chem = float(request.POST['Chem'])
        math = float(request.POST['Math'])

        marks = [phy, chem, math]

        std = Student(name, marks)

        avg = std.calculate_average()
        avg_grd = std.assign_grade()

        return render(request, 're.html', {'marks': avg, 'grade': avg_grd})

