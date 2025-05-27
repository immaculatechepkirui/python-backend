class Pupil:
    name = "Immah"
    age = 19
    school = "AkiraChix"
    country = "Kenya"



class Student():
    school = "AkiraChix"
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.year = 2025 - age
        self.marks= []


    def greet_student(self):
        print(f"Hello {self.first_name}, welcome to {self.school}")

    def initials(self):
        print(self.first_name[0],self.last_name[0])

    def total_marks(self, points):
        self.marks.append(points)
        total = 0
        for point in self.marks:
            total += point
            return total

