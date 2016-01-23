import pygame,sys
from random import randint
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
blue=(55,155,255)
yellow=(255,150,0)
pygame.init()

size=700,500
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")
back=pygame.image.load("bg.jpg")
back_rect=back.get_rect()
done=False

clock=pygame.time.Clock()

def ball(x,y):
    pygame.draw.circle(screen,yellow,[x,y],20)


def gameover():
    font=pygame.font.SysFont(None,75)
    text=font.render("Game Over",True,red)
    screen.blit(text,[150,250])

def obstacle(xloc,yloc,xsize,ysize):
    pygame.draw.rect(screen,green,[xloc,yloc,xsize,ysize])
    pygame.draw.rect(screen,green,[xloc,int(yloc+ysize+space),xsize,ysize+500])

def Score(s):
    font=pygame.font.SysFont('freesansbold.ttf',55)
    text=font.render("Score:"+str(s),True,black)
    screen.blit(text,[0,0])

x=350
y=250
score=0
x_speed=0
y_speed=0
ground=477
xloc=700
yloc=0
xsize=70
ysize=randint(0,300)
space=150
obspeed=4.5
while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_speed=-10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_speed=5
    screen.fill(blue)

    #screen.blit(back,back_rect)

    obstacle(xloc,yloc,xsize,ysize)
    ball(x,y)
    Score(score)
    y+=y_speed
    xloc-=obspeed
    if y > ground:
        gameover()
        y_speed=0
        obspeed=0
    if xloc <-80:
        xloc=700
        ysize=randint(0,400)

    if x+20> xloc and y-20 < ysize and x-15 <xsize+xloc:
        gameover()
        y_speed=0
        obspeed=0

    if x+20> xloc and y+20 > ysize+space and x-15 <xsize+xloc:
        gameover()
        y_speed=0
        obspeed=0

    if x>xloc and x< xloc+3:
        score=score+1
    pygame.display.flip()
    clock.tick(60)

