class Circle:
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi
    
    def area(self):
        return self.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * self.pi * self.radius
    
    def display(self):
        print("Circle with radius:", self.radius)
        print("Area:", self.area())
        print("Perimeter (Circumference):", self.perimeter())


radius = float(input("Enter the radius of the circle: "))
pi = float(input("Enter the value of pi: "))
circle = Circle(radius, pi)
circle.display()
