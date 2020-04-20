import pygame,sys,time,random
from pygame import *

window=pygame.display.set_mode((800,600))
pygame.display.set_caption("Pong")
screen=pygame.display.get_surface()
screen.fill((0,0,0))

clock=pygame.time.Clock()
FPS=25

pygame.init()

def drawball(ballX,ballY):
    if(ballX<=10):
        ballX=10
    if(ballX>=790):
        ballX=790
    
    pygame.draw.circle(screen,(255,255,0), (ballX,ballY),10)
    


    
def myquit():
    pygame.quit()
    sys.exit(0)

def gameloop():
    x=100
    y=500
    upper=False
    lower=False
    ballX=100
    ballY=100
    ball_change_x=5
    ball_change_y=5
    score=0
    gameOver=False
    while True:
        while gameOver:
            font= pygame.font.SysFont('comicsansms', 30, False, True)
            text = font.render("Your Score = "+str(score) , True, (255,200,200))
            screen.blit(text,[300,150])
            msg = font.render("PRESS C TO CONTINUE AND Q TO QUIT" , True, (255,200,200))
            screen.blit(msg,[100,350])
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    myquit()
                if(event.type==pygame.KEYDOWN):
                    if(event.key==pygame.K_q):
                        myquit()
                    elif(event.key==pygame.K_c):
                        gameloop()

            pygame.display.flip()


        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                myquit()
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_q):
                    myquit()
                elif(event.key==pygame.K_LEFT):
                    x=x-40
                elif(event.key==pygame.K_RIGHT):
                    x=x+40
        if(x>=720):
            x=720
        if(x<=0):
            x=0
        pygame.display.update()
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255,10,10),[x,y,80,20])
        pygame.draw.rect(screen, (255,255,255), [0,520,800,80])
        pygame.display.update()
        
        ballX += ball_change_x
        ballY += ball_change_y
        if ballX<0:
            ballX=0
            ball_change_x = ball_change_x * -1
        elif ballX>785:
            ballX=785
            ball_change_x = ball_change_x * -1
        elif ballY<0:
            ballY=0
            ball_change_y = ball_change_y * -1
        elif ballX>x and ballX<x+100 and ballY==500:
            ball_change_y = ball_change_y * -1
            score = score + 1
        elif ballY>500:
            ball_change_y = ball_change_y * -1
            gameOver=True      
        drawball(ballX,ballY)
        pygame.display.update()

        font= pygame.font.SysFont(None, 40, False, False)
        text = font.render("Score = "+str(score) , True, (0,200,200))
        screen.blit(text,[300,550])  
        pygame.display.flip()

        pygame.display.update()
        clock.tick(FPS)
        



gameloop()