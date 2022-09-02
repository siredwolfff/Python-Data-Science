import pgzrun
from random import randint

WIDTH = 700
HEIGHT = 500

p = Actor('char1',(50,200))
c= Actor('char2',(randint(0, WIDTH), randint(0 , HEIGHT) ))
e = Actor('item1')
speed = 7 #speed of movement
espeed = 2
score = 0 # global variable

is_game_started= True
is_game_over= False

def draw():
    if not is_game_started and not is_game_over:
        screen.fill('yellow')
        screen.draw.text('MY GAME',center=(WIDTH//2 , HEIGHT//2), color ='red',fontsize=100)
        screen.draw.text('Press space to start',center=(WIDTH//2 , HEIGHT//2+50), color ='red' )

    elif  is_game_started and not is_game_over:
        screen.fill("white")
        screen.draw.text(f'Score: {score}',(20,20))
        p.draw()
        e.draw()
        c.draw()
    elif is_game_over:
        pass

def update():
    player_controls()
    check_score()
    enemy_movement()

def enemy_movement():
    if p.x > e.x:
        e.x += espeed
    if p.y > e.y:
        e.y += espeed
    if p.x < e.x:
        e.x -= espeed
    if p.y < e.y:
        e.y -= espeed
    if p.colliderect(e):
        print("game over")

     
        

def check_score():
    global score
    if p.colliderect(c):
        score += 100
        c.pos = (randint(0, WIDTH), randint(0 , HEIGHT))
        sounds.s1.play()




def player_controls():
    if keyboard.UP and not p.top < 0:
        p.y += -speed
        p.angle = 0 
    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y += speed
        p.angle = 0
    elif keyboard.LEFT and not p.left < 0:
        p.x += -speed
        p.angle = 10
    elif keyboard.RIGHT and not p.right > WIDTH:
        p.x += speed
        p.angle = -10
    else:
        p.angle = 0

pgzrun.go()