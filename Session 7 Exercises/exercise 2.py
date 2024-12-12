##Use inheritance to create a parent class Shape and a child class Rectangle. Add a method to calculate the area of the rectangle.

class Shape:
    def __init__(self):
        print("This is a shape")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example
rect = Rectangle(5, 4)
print("Area of rectangle:", rect.area())
