import pygame,sys,time,random
from pygame import *

window_width=800
window_height=600
window=pygame.display.set_mode((800,600))
screen=pygame.display.get_surface()

clock = pygame.time.Clock()
FPS = 5

def message_to_score(msg, color):
    global screen
    font=pygame.font.SysFont(None, 40, bold=True, italic=True)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [200, 150]) 

def message_to_continue(msg, color):
    global screen
    font=pygame.font.SysFont(None, 30, bold=True, italic=True)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [200, 250])

def message_to_quit(msg, color):
    global screen
    font=pygame.font.SysFont(None, 30, bold=True, italic=True)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [200, 350]) 

def myquit():
    pygame.quit()
    sys.exit(0)

def snake(snakelist):
    global screen
    for size in snakelist:
        pygame.draw.rect(screen, (255,255,255),[size[0]+5,size[1],20,20],2)

pygame.init()
def gameloop():
    global x,y,window_height,window_width,screen
    snakelist=[]
    catx=0
    caty=0
    x=100
    y=100
    snakeLength=1
    randomX = round(random.randrange(0, window_width-20)/10.0)*10.0
    randomY = round(random.randrange(0, window_height-20)/10.0)*10.0 
    gameOver=False
    while True:
        screen.fill((0,0,0))
        while gameOver == True:
            screen.fill((255,0,0))
            message_to_score("YOUR SCORE IS :"+str(snakeLength),(255,255,255))
            message_to_continue("PRESS C TO RESTART ",(255,255,255))
            message_to_quit("PRESS Q TO QUIT ",(255,255,255))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    myquit()              
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        myquit()
                    if event.key == pygame.K_c:
                        gameloop() 
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                myquit()
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_LEFT):
                    catx = -20
                    caty = 0
                elif(event.key==pygame.K_RIGHT):
                    catx = 20
                    caty = 0
                elif(event.key==pygame.K_UP):
                    catx = 0
                    caty = -20
                elif(event.key==pygame.K_DOWN):
                    catx = 0
                    caty = 20
            if(x<0 or x>window_width or y<0 or y>window_width):
                gameOver=True
        x+=catx
        y+=caty
        pygame.draw.rect(screen,(0,255,255),[randomX,randomY,20,20], 2)
        pygame.display.update()
        temp=[]
        temp.append(x)
        temp.append(y)
        snakelist.append(temp)
        if(len(snakelist)>snakeLength):
            del snakelist[0]
        snake(snakelist)
        pygame.display.update()
        
        if(x>=randomX and x<=randomX+20):
            if(y>=randomY and y<=randomY+20):
                randomX = round(random.randrange(0, window_width-20)/10.0)*10.0
                randomY = round(random.randrange(0, window_height-20)/10.0)*10.0
                snakeLength+=1

    
        
        clock.tick(FPS)
            
gameloop()