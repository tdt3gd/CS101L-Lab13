import turtle

class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

    def draw_action(self):
        """ Draws a box """
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)

class BoxFilled(Box):
    def __init__(self, x2, y2, width, height, color, fillcolor):
        super().__init__(x2, y2, width, height, color)
        self.fillcolor = fillcolor
        turtle.fillcolor = self.fillcolor
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x3, y3, radius, color):
        super().__init__(x3, y3, color)
        self.radius = radius
        turtle.circle(self.radius)
        Circle.draw_action(self)

class CircleFilled(Circle):
    def __init__(self, x3, y3, radius, color, fillcolor):
        super().__init__(x3, y3, radius, color)
        turtle.fillcolor = fillcolor
        turtle.begin_fill()
        turtle.circle(self.radius)
        CircleFilled.draw_action(self)
        turtle.end_fill()
        
            
        
