import pygame as game
from sys import exit
import random
import time
game.init()  
game.font.init() 
screen = game.display.set_mode((800,800))
clock = game.time.Clock()
screen.fill("White")


#cordinates of the vertices of the original triangle
Ax,Ay = 400,100
Bx,By = 50,650 
Cx,Cy = 750,650
Xs = [Ax,Bx,Cx]
Ys = [Ay,By,Cy]

x= 400 
y =372   
game.display.set_caption("Sierpinski Triangle")


#intro screen
banner = game.font.Font("nostalgic_remain/regular.ttf",80)
banner_text = banner.render("  Sierpinski",False,"Black")
banner_text2 = banner.render("   Triangle",False,"Black")
banner_rect = game.Rect(200,200,400,400)
flag  = True 
white = game.image.load("white background.png")
WHITE  = game.transform.scale(white,[800,800])

while True:
    for event in game.event.get():
        if event.type==game.QUIT:
            game.quit()
            exit()
    if flag:
        screen.blit(banner_text,banner_rect)
        screen.blit(banner_text2,(200,300))
        game.display.update()
        time.sleep(1)
        screen.blit(white,(200,200))
        flag  = False
        
    else:

        #Original triangle
        game.draw.line(screen,"Black",(400,100),(50,650), 4)
        game.draw.line(screen,"Black",(750,650),(50,650), 4)
        game.draw.line(screen,"Black",(400,100),(750,650), 4)
        a =random.randint(0,2)
        background = screen.copy()
        game.draw.line(screen,"Green",(Xs[a],Ys[a]),(x,y),1)
        game.display.update()
        game.time.wait(200)
        screen.blit(background,(0,0))
        game.draw.circle(screen,"Black",(x,y),1)
        x = int((x+Xs[a])/2)
        y = int((y+Ys[a])/2)
    
    clock.tick(6000)
    game.display.update()