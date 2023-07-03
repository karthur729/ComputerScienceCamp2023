import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Define colors
colors = ["red", "green", "blue", "orange", "purple"]

# Move the turtle in a circular pattern
for _ in range(36):
    my_turtle.color(colors[_ % len(colors)])  # Select a color from the list
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.right(90)
    my_turtle.right(10)  # Rotate the turtle by 10 degrees

# Exit the turtle graphics window
turtle.done()
