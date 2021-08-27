import pygame, random

class Ghost:
    speed=5
    g=0.5
    rect= pygame.Rect(300,250,100,100)
    def gravity(self):
        self.speed=self.speed+self.g
        self.rect.y= self.rect.y + self.speed
    def jump(self):
        self.speed=-10
   
    def moveRight(self):
        self.rect.x+=20
        
    def moveLeft(self):
        self.rect.x-=20
    
    def display(self):
        screen.blit(images["ghost"],self.rect) 
        
class Door:
   
    def __init__(self,y): 
        self.speed=3
        self.gap=random.randint(100, 400)
        self.rect1=pygame.Rect(self.gap,y+100,40,120)
        self.rect2=pygame.Rect(self.gap,y+240,100,5)
        
    def display(self):  
        screen.blit(images["door"],self.rect1)
    
    def move(self):
        self.rect1.y+=self.speed
        self.rect2.y+=self.speed
        if(self.rect1.y>600):
            self.rect1.y =-200
            self.rect2.y=-60
            self.rect1.x=random.randint(100, 500)
            self.rect2.x=self.rect1.x

pygame.init()
clock=pygame.time.Clock()

width=600
height=600
screen = pygame.display.set_mode((width,height))
  
images={}
images["ghost"] = pygame.image.load("ghost.png").convert_alpha()
images["door"] = pygame.image.load("door.png").convert_alpha()

groundy=-50
score=0
score_font=pygame.font.Font('freesansbold.ttf', 25)
            
state="play"

'''
Create ghost object and d1 & d2 objects
'''

while True:    
    screen.fill((50,150,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ghost.jump()
            # Create event based movement for ghost similar one created above in order to use the methods in class Ghost declared above.
        
    if state=="play":          
        groundy=groundy+3 
        if groundy>=0:
            groundy=-125                  
        ghost.gravity() 
        
        d1.move()
        d1.display()
        
        # use move and display on d2 object
        
        ghost.display()
        
    if state=="over":
        over_text=score_font.render("Game Over", False, (255,255,0))  
        screen.blit(over_text,[230,250])
    
    if ghost.rect.colliderect(d1.rect2) or ghost.rect.colliderect(d2.rect2):
        state="over"
    
    pygame.display.update() 
    clock.tick(30) 
