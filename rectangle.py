class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area =     self.length * self.width
        return area

    def perimeter(self):
        perimeter =  2 * (self.length + self.width)
        return perimeter


rect = Rectangle(7, 5)
a = rect.area()
b = rect.perimeter()

print("Area =", a)
print("Perimeter =", b)
