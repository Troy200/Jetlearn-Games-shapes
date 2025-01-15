import pgzrun 
import random
WIDTH=300
HEIGHT=300

def draw():
    screen.fill("light blue")

    screen.draw.filled_circle((150,150),130,"black")
    
    s=120


    for i in range(5):


        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)


        screen.draw.filled_circle((150,150),s,(r,g,b))
        
        
        s=s-30









pgzrun.go()