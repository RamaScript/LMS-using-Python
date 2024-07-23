#W.A.P. to create list of object of 5 students and display the details of students having maximum marks

class Student:
    def get_details(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

students = []
n = int(input("Enter The number of students : "))
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    roll_number = int(input(f"Enter roll number of student {i+1}: "))
    marks = int(input(f"Enter marks of student {i+1}: "))
    
    student = Student()
    student.get_details(name, roll_number, marks)
    students.append(student)

max_marks_student = students[0]
for student in students:
    if student.marks > max_marks_student.marks:
        max_marks_student = student

print("Details of the student with maximum marks:")
max_marks_student.show_details()
