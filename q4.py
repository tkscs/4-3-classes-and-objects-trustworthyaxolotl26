import turtle

class Point:
    """a point class with mutable methods: scale sheer, and shift"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        print(f"{self.x}, {self.y}")
    def draw(self):
        turtle.goto(self.x, self.y)
        turtle.up()
        turtle.dot()
        turtle.write(str(f"{self.x}, {self.y}"))
    def scale(self, constant):
        self.x = self.x*constant
        self.y = self.y*constant
    def sheer(self, x_mult, y_mult):
        self.x = self.x*x_mult
        self.y = self.y*y_mult
    def shift(self, z=0, t=0):
        self.x = self.x+z
        self.y = self.y+t
    # def add(self):
    #     self.x = int(p1.x + p2.x)
    #     self.y = int(p1.y + p2.y)

p1 = Point(0, 0)
p2 = Point(0, 100)
p3 = Point(100, 0)
p4 = Point(100, 100)
# p5 = Point(p1.add(), p1.add())

p1.draw()
p2.draw()
p3.draw()
p4.draw()

# p1.scale(-1)
# p2.scale(-1)
# p3.scale(-1)
# p4.scale(-1)

# p1.sheer(2, 3)
# p2.sheer(2, 3)
# p3.sheer(2, 3)
# p4.sheer(2, 3)

p1.shift(5, 5)
p2.shift(-5, 5)
p3.shift(5, -5)
p4.shift(-5, -5)

p1.draw()
p2.draw()
p3.draw()
p4.draw()
# p5.draw()

for i in range(100):
    p1.shift(5, 5)
    p2.shift(-5, 5)
    p3.shift(5, -5)
    p4.shift(-5, -5)
    p1.draw()
    p2.draw()
    p3.draw()
    p4.draw()



turtle.exitonclick()