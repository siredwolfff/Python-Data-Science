import pgzrun

WIDTH = 1000    
HEIGHT = 1000

box = Rect((50,150), (50,100))
box2 = Rect((105,150),(50,50))


def draw():
    screen.fill('white')
    screen.draw.text('hola amigos', (50,50), color = 'white')
    screen.draw.text('This is game programming', (50,80), color = 'yellow', fontsize = 50)
    screen.draw.rect(box, color ='white')
    screen.draw.filled_rect(box2, color='yellow')

def update():
    box.x+= 1
    box2.y += 2


pgzrun.go()
