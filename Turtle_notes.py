import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape("turtle")
my_turtle.speed(0)


my_screen = turtle.Screen()
my_screen.bgcolor("white")

# draw a shape using goto
my_turtle.fillcolor("pink")
my_turtle.begin_fill() # starts a shape to fill in
my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.end_fill() # end of shape

# pick up the turtle
my_turtle.up()
my_turtle.goto(200, 200)

my_turtle.fillcolor("green")
my_turtle.begin_fill()
my_turtle.down()
my_turtle.goto(300, 300)
my_turtle.goto(300, 200)
my_turtle.goto(200, 200)
my_turtle.end_fill()

# draw using headings
my_turtle.up()
my_turtle.goto(0, 0)
my_turtle.down()
my_turtle.width(1) # width in pixels

my_turtle.fillcolor("yellow")
my_turtle.begin_fill()
my_turtle.forward(100)
my_turtle.setheading(90)
my_turtle.forward(100)
my_turtle.setheading(180)
my_turtle.forward(100)
my_turtle.setheading(270)
my_turtle.forward(100)
my_turtle.end_fill()

for i in range(6):
    my_turtle.right(60)
    my_turtle.forward(100)
    my_turtle.down()


# Rectangle recursive pattern
my_screen.clear()

my_turtle.home()

def recursive_rect(width, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(width / 2, height / 2)
        my_turtle.down()
        my_turtle.begin_fill()
        my_turtle.fillcolor("pink")
        my_turtle.goto(width / 2, -height / 2)
        my_turtle.goto(-width / 2, -height / 2)
        my_turtle.goto(-width / 2, height / 2)
        my_turtle.goto(width / 2, height / 2)
        my_turtle.end_fill()
        recursive_rect(width / 1.5, height / 1.5, depth - 1)


recursive_rect(1000, 2000, 10)




my_screen.clear()

# Recursive Fractal (ncaa)

def recursive_ncaa(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + size, y)
        my_turtle.goto(x + size, y + size / 2)
        my_turtle.goto(x + size, y - size / 2)
        recursive_ncaa(x + size, y + size / 2, size / 2, depth - 1)
        recursive_ncaa(x+ size, y - size / 2, size / 2, depth - 1)


recursive_ncaa(-300, 0, 200, 7)



my_screen.exitonclick()