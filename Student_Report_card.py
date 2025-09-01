"""
Student Report Card

Class: Student with attributes (name, roll_no, grades).

Methods: add_grade(), calculate_average(), display_report().

"""


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.grades = []

    def add_grade(self, subject, grade):
        self.grades.append((subject, grade))  # store it as tuple

    def calculate_average(self):
        total = sum(
            [grade for _, grade in self.grades]
        )  # for _ takes the placeholder (subject) #it is called placeholder
        return total / len(self.grades) if self.grades else 0

    def display_report(self):
        print(f"\n Report card {self.name} (Roll no:{self.roll_no})")
        for subject, grade in self.grades:
            print(f"{subject}: {grade}")
        print(f"Average: {self.calculate_average():.2f}")


# example for output
s1 = Student("Rahul", 101)
s1.add_grade("Math", 85)
s1.add_grade("Science", 90)
s1.add_grade("English", 78)
s1.display_report()
