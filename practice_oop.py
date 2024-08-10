class circle:
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return (3.14) * self.rad**2

    def perimeter(self):
        return 2 * 3.14 * self.rad


c1 = circle(22)
print(c1.rad)
print("The radius is : ", c1.area())
print("The perimeter of the circle is : ", c1.perimeter())
