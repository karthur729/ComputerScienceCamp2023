import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Move the turtle forward to draw the square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Exit the turtle graphics window
turtle.done()
