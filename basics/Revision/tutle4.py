from turtle import *

for i in range(6):
        pencolor('blue')
        forward(75)
        pencolor('red')
        circle(25)
        pencolor('blue')
        left(360/6)
        write("Deepak", font=('Verdana', 14, 'bold'))

mainloop()