import turtle

t = turtle.Turtle()
t.speed(5)
t.pensize(3)

# --- Flag outline ---
t.penup()
t.goto(-250, 200)
t.pendown()

t.color("red")
t.begin_fill()

t.goto(-250, 200)
t.goto(80, 20)
t.goto(-250, 20)
t.goto(80, -160)
t.goto(-250, -160)
t.goto(-250, 200)

t.end_fill()

# --- Blue border ---
t.color("blue")
t.pensize(6)

t.penup()
t.goto(-250, 200)
t.pendown()

t.goto(80, 20)
t.goto(-250, 20)
t.goto(80, -160)
t.goto(-250, -160)
t.goto(-250, 200)

# --- Moon ---
t.penup()
t.goto(-145, 80)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(35)
t.end_fill()

# Cover part of moon to make crescent
t.penup()
t.goto(-130, 90)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(35)
t.end_fill()

# --- Sun ---
t.penup()
t.goto(-145, -75)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(25)
t.end_fill()

# Sun rays
t.color("white")
for i in range(12):
    t.penup()
    t.goto(-145, -50)
    t.setheading(i * 30)
    t.pendown()
    t.forward(45)

t.hideturtle()
turtle.done()
