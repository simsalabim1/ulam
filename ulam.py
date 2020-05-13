
user=int(input("what angle of turning in your spiral?"))
num=int(input("how many times should it run?"))
len=int(input('what is the starter length'))

type=input("please write 1, 2, 3or 4 for a blue,green,red or rainbow tyme")
if type== '1':
    colors = ["lightblue", "blue", "cyan", "darkcyan", "teal","aqua"]
elif type== '2':
    colors = ["lime", "honeydew", "darkgreen", "limegreen", "green","mintcream"]
elif type== '3':
    colors = ["red", "maroon", "indianred", "salmon", "firebrick","chocolate"]
elif type=='4':
    colors = ['red','purple', 'blue', 'green', 'yellow','orange']
import random
import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)
t.width(2.5)



for i in range(0,num):
    color = random.choice(colors)
    t.color(color)
    t.forward(len)
    t.right(user)
    len = len + 5
turtle.getscreen()._root.mainloop()

