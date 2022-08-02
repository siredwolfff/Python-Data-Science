from turtle import *

speed('fast')
bgcolor('black')

side = 150
size = 7


for i in range(size):
    pencolor('green')
    forward(150)
    left(360/size)
    pencolor('red')
    circle(15)
    write(i, font=('Arial', 15,'italic'))

mainloop()