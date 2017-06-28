
import pygame
import random
import sys
class Ball:


    def __init__(self,X,Y):

        self.velocity = [1,1]
        self.ball_image = pygame.image.load ('palla1.png'). convert_alpha()
        self.ball_boundary = self.ball_image.get_rect (center=(X,Y))
        self.ball_center = [(self.ball_boundary.left+self.ball_boundary.right)/2,(self.ball_boundary.top+self.ball_boundary.bottom)/2]

    
        self.rect = self.ball_image.get_rect (center=(X,Y))


def distanza(a,b):
    d = (b.ball_center[1]-a.ball_center[1]) * (b.ball_center[1]-a.ball_center[1]) + (b.ball_center[0]-a.ball_center[0]) * (b.ball_center[0]-a.ball_center[0])
    
    return d    
    
    

if __name__ =='__main__':

    width = 1000
    height = 800
    background_colour = 0,0,0
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Palle rimbalzanti")
    num_balls = 5

    
    
    ball_list = []
    palla = Ball(random.randint(90, (width - 90)),random.randint(90, (height - 90)))
    ball_list.append(palla)
    palla = ball_list[0]
    raggio = (palla.ball_boundary.right - palla.ball_boundary.left)/2


    #fa una lista con tutte le palle
    for number in range(1,num_balls): #fino al numero desiderato
        palla = Ball(random.randint(90, (width - 90)),random.randint(90, (height - 90))) #crea una nuova palla
        for i in range(1,len(ball_list)+1):#confronto con le palle già presenti nella lista
                print('indice: ', i, 'lunghezza: ', len(ball_list), 'number: ', number)
                if distanza(ball_list[number - i], palla) > 4*raggio*raggio: #se le palle sono abbastanza distanti
                    if i == len(ball_list): #se c'è stato il confronto di palla con tutte le palle nella lista
                        ball_list.append( palla )
                        ball_list[number].velocity = [random.randint(-10,10),random.randint(-10,10)]
                    else:
                        continue #continua il confronto
                else:
                    number -= 1 #fa restare invariato number col proseguimento del ciclo
                    break
        

    print('lunghezza', len(ball_list))
                
            
        


        
    while True:
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                        sys.exit(0)
        window.fill (background_colour)

#rimbalzo sui muri
        
        for ball in ball_list:
                if ball.ball_boundary.left < 0 or ball.ball_boundary.right > width:
                        
                        ball.velocity[0] = -ball.velocity[0]
                if ball.ball_boundary.top < 0 or ball.ball_boundary.bottom > height:
                        
                        ball.velocity[1] = -ball.velocity[1]

                for ball1 in range(num_balls-1):
                    for ball2 in range(ball1+1,num_balls):
                        if distanza(
                            ball_list[ball1],ball_list[ball2]) < 4*raggio*raggio:

                            
                            ball_list[ball1].velocity[0] = -ball_list[ball1].velocity[0]
                            ball_list[ball1].velocity[1] = -ball_list[ball1].velocity[1]
                            ball_list[ball2].velocity[0] = -ball_list[ball2].velocity[0]
                            ball_list[ball2].velocity[1] = -ball_list[ball2].velocity[1]

                
                #muovere la palla
                ball.ball_boundary = ball.ball_boundary.move (ball.velocity)
                ball.ball_center = [(ball.ball_boundary.left+ball.ball_boundary.right)/2,(ball.ball_boundary.top+ball.ball_boundary.bottom)/2]
               
                #metterla su schermo
                window.blit (ball.ball_image, ball.ball_boundary)
        pygame.display.flip()
