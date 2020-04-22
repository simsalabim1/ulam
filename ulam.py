user=int(input("what angle?"))
import random
import turtle
t = turtle.Turtle()
colors = ["red", "yellow", "green", "blue", "purple","cyan"]
t.width(2.5)


len=5
for i in range(100):
    color = random.choice(colors)
    t.color(color)
    t.forward(len)
    t.right(user)
    len = len + 5
t.mainloop()
