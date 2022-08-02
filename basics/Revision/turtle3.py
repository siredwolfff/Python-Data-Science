from turtle import *

bgcolor('black') #background color
side=8
angle= 360/ side 
color('blue') # color to be filled
pencolor('red') # color of pen

speed('fastest') # turtle speed
 
begin_fill()  #starting point to fill the color
for i in range(side):
    
    forward(150)
    
    left(angle)
    
end_fill() #ending point to fill the color

mainloop()