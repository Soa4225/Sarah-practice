""""
GCIS-123-603
    Prof.Ali Assi.
Activity 1:
Group 1:
    Sarah Arab
    Tannya Navani
    Farah Albanna
This activity is mainly done using turtle python to draw the following 
shapes hexagon,circle,square by asking the user to input the color for 
the shapes and border.
"""

import turtle

def setPos(turta, x, y):
    turta.penup()
    turta.goto(x, y)
    turta.pendown()


def hexagon(turta, fill_color, border_color):
    turta.fillcolor(fill_color)
    turta.pencolor(border_color)
    turta.begin_fill()
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)

    
    turta.end_fill()

def square(turta, fill_color, border_color):
    turta.fillcolor(fill_color)
    turta.pencolor(border_color)
    turta.begin_fill()
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.end_fill()

def circle(turta, fill_color, border_color):
    turta.fillcolor(fill_color)
    turta.pencolor(border_color)
    turta.begin_fill()
    turta.circle(50)
    turta.end_fill()

def pattern(turta, hexa_pos, circle_pos, square_pos, hexa_fill_color,circle_fill_color,square_fill_color, border_color):
    setPos(turta, hexa_pos[0], hexa_pos[1])
    hexagon(turta, hexa_fill_color, border_color)
    
    setPos(turta, circle_pos[0], circle_pos[1])
    circle(turta, circle_fill_color, border_color)
    
    setPos(turta, square_pos[0], square_pos[1])
    square(turta, square_fill_color, border_color)

def drawPattern(turta, positions):
    hexa_fill_color = input("Enter fill color for hexagon: ")
    circle_fill_color = input("Enter fill color for circle: ")
    square_fill_color = input("Enter fill color for square: ")
    border_color = input("Enter border color for all shapes: ")

    for pos in positions:
        pattern(turta, pos[0], pos[1], pos[2],hexa_fill_color,circle_fill_color,square_fill_color, border_color)

def main():
    screen.bgcolor("white")
    turta = turtle.Turtle()
    turta.speed(3)
    screen.setup(width=800,height=800)
    screen = turtle.Screen()
    positions = [
        [[-180, 220], [0, 120], [100, 210]],
        [[-100, 100], [80, 0], [180, 90]],
        [[-20, -20], [160, -120], [260, -30]]
    ]

    drawPattern(turta, positions)

    turta.hideturtle()
    turtle.done()
main()
