import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        print(self.x, self.y)
    def draw(self):
        turtle.goto(self.x, self.y)
        turtle.up()
        turtle.dot()
    def add(self):
        self.x = int(p1.x + p2.x)
        self.y = int(p1.y + p2.y)

p1 = Point(0, 0)
p2 = Point(0, 100)
p3 = Point(100, 0)
p4 = Point(100, 100)
p5 = Point(p1.add(), p1.add())

p1.draw()
p2.draw()
p3.draw()
p4.draw()
p5.draw()

turtle.exitonclick()