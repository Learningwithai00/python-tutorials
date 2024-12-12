##Create a Student class with attributes like name and age and a method to display the student’s details.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Example
student = Student("Alice", 20)
student.display_details()
