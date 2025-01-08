import pgzrun 
import random
WIDTH= 600
HEIGHT=600

def draw():
    screen.fill("white")
    w=600
    h=100

    for i in range(9):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)

        r1=Rect((0,250),(w,h))
        r1.center=(300,300)
        screen.draw.rect(r1,(r,g,b))
        w=w-60
        h=h+60

        







pgzrun.go()