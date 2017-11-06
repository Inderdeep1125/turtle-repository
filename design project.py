#inderdeep
import turtle
bob = turtle.Turtle()
sides = 20
angle = 360/20
distance = 50
bob.width(5)
bob.speed(11)
turtle.bgcolor("black")
for times in range(3):
    print(times*2+6)




bob.circle(20)
for times in range(200):
    bob.forward(times*2+1)
    bob.left(290)
    bob.color("light green")
    bob.forward(times*2+1)
    bob.left(290)
    bob.color("white")
    bob.forward(times*2+1)
    bob.left(290)
    bob.color("red")
    
    
