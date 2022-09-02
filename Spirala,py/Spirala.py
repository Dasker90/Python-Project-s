import turtle
import random
t=turtle.Turtle()
t.speed("fastest")
colo=["yellow","blue","pink","red","orange","green","black","violet"]
def check(new):
    global t
    new+=10
    t.setheading(new)
    t.circle(100)
t.circle(100)
for i in range (100):
    t.color(random.choice(colo))
    check(t.heading())

turtle.Screen().exitonclick()
        
