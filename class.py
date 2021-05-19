from math import pi
class Shapes:
    def __init__(self, name, side):
        self.name = name
        self.side = side

    def Area(self):
        print('I am a: ' + self.name + '\n' +
              'I have: ' + self.side + 'sides')


obj_shapes = Shapes('shapes', 'so many')
obj_shapes.Area()

class Rectangle(Shapes):
    def __init__(self, length1, width1):
        self.length = length1
        self.width = width1

    def Area(self):
        result = self.length * self.width
        print(result)


obj_book = Rectangle(10, 7)
obj_book.Area()

class Circle(Shapes):
    def __init__(self, radius):
        self.pi = 3.14
        self.radius = radius

    def Area(self):
        result1 = self.radius**2 * self.pi
        print(result1)


obj_radius_area = Circle(15)
obj_radius_area.Area()


class Triangle(Shapes):

    def __init__(self, base, height):
        self.base = base/2
        self.height = height

    def Area(self):
        result2 = self.base * self.height
        print(result2)


obj_three_sides = Triangle(20, 12)
obj_three_sides.Area()
