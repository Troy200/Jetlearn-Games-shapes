import pgzrun

WIDTH=300
HEIGHT=300

def draw():
    screen.fill(" light blue")

    r=Rect((150,150),(150,100))
    r.center=(150,150)
    #screen.draw.rect(r,"black")
    screen.draw.filled_rect(r,"black")




pgzrun.go()
