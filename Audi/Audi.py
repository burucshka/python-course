import turtle as a
a.speed(4)
a.width(10)
def draw_circle():
    a.circle(60)
a.penup()
a.goto(-180, 0)
a.pendown()
for i in range(4):
    draw_circle()
    a.penup()
    a.fd(80)
    a.pendown()
a.hideturtle()