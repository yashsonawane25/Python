import turtle
import math
# def square(t):
#     """Make turtle t draw a square."""
#     for _ in range(100):
#         t.forward(100)  # Move forward by 100 units
#         t.left(90)      # Turn left by 90 degrees

# # Create a turtle instance named bob
# bob = turtle.Turtle()

# # Call the square function and pass bob as an argument
# square(bob)

# # Keep the window open until it is closed by the user
# turtle.done()


# def square(t, length):
#     """Make turtle t draw a square with sides of length."""
#     for _ in range(4):
#         t.forward(length)  # Move forward by length units
#         t.left(90)         # Turn left by 90 degrees

# # Create a turtle instance named bob
# bob = turtle.Turtle()

# # Call the square function and pass bob and the length as arguments
# square(bob, 150)  # Change 150 to any other value to test different side lengths

# # Keep the window open until it is closed by the user
# turtle.done()

# length =30
# angle = 60
# def polygon (t, n,length):
#     angle= 360 / n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)

# polygon(7 ,70)




# def polygon(t, length, n):
#     """Make turtle t draw a regular polygon with n sides of length."""
#     angle = 360 / n  # Calculate the exterior angle for the polygon
#     for _ in range(n):
#         t.forward(length)
#         t.left(angle)

# # Create a turtle instance named bob
# bob = turtle.Turtle()

# # Call the polygon function and pass bob, the length, and the number of sides as arguments
# polygon(bob, 100, 6)  # Change 100 and 6 to test different side lengths and number of sides

# # Keep the window open until it is closed by the user
# turtle.done()


# for circle
def circle(t,r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
bob = turtle.Turtle()

# # Call the polygon function and pass bob, the length, and the number of sides as arguments
polygon(bob, 100, 6)  # Change 100 and 6 to test different side lengths and number of sides

# # Keep the window open until it is closed by the user
turtle.done()
