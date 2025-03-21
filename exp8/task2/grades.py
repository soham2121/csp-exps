class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        total_marks = sum(self.marks)
        num_subjects = len(self.marks)
        if num_subjects == 0:
            return 0
        return total_marks / num_subjects

    def assign_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F' 