import turtle

class Point:
    """a point class with mutable methods: scale sheer, and shift"""
    def __init__(self, x, y, label=""):
        self.x = x
        self.y = y
        self.label = label
    def __str__(self):
        return self.label
    def draw(self):
        turtle.goto(self.x, self.y)
        turtle.up()
        turtle.dot()
        turtle.write(str(f"{self.x}, {self.y} - {self.label}"))
    def scale(self, constant):
        # self.x = self.x*constant
        # self.y = self.y*constant
        x = self.x*constant
        y = self.y*constant
        pNEW = Point(x, y, label = f"{constant}({str(self)})")
        return pNEW
    def add(self, another_point):
        x = self.x+another_point.x
        y = self.y+another_point.y
        label = f"{str(self)}+{str(another_point)}"
        newer_point = Point(x, y, label)
        return newer_point
    # def sheer(self, x_mult, y_mult):
    #     # self.x = self.x*x_mult
    #     # self.y = self.y*y_mult
    # def shift(self, z=0, t=0):
    #     # self.x = self.x+z
    #     # self.y = self.y+t
    # # def add(self):
    # #     self.x = int(p1.x + p2.x)
    # #     self.y = int(p1.y + p2.y)

p1 = Point(0, 0, "p1")
p2 = Point(0, 100, "p2")
p3 = Point(100, 0, "p3")
p4 = Point(100, 100, "p4")
# p5 = Point(p1.add(), p1.add())

p1.draw()
p2.draw()
p3.draw()
p4.draw()

# scaled_p1 = p1.scale(2)
# scaled_p2 = p2.scale(2)
# scaled_p3 = p3.scale(2)
# scaled_p4 = p4.scale(2)

# scaled_p1.draw()
# scaled_p2.draw()
# scaled_p3.draw()
# scaled_p4.draw()

p5 = p4.add(p2)

# # p1.sheer(2, 3)
# # p2.sheer(2, 3)
# # p3.sheer(2, 3)
# # p4.sheer(2, 3)

# # p1.shift(5, 5)
# # p2.shift(-5, 5)
# # p3.shift(5, -5)
# # p4.shift(-5, -5)

# p1.draw()
# p2.draw()
# p3.draw()
# p4.draw()
p5.draw()

turtle.exitonclick()