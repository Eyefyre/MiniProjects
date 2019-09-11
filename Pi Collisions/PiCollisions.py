import pygame, math, os
pygame.init()
ScreenWidth = 640
ScreenHeight = 480
win = pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption("Pi Collisions")
Boxfont = pygame.font.Font('freesansbold.ttf', 12) 
Countfont = pygame.font.Font('freesansbold.ttf', 24) 
ClackPath = os.path.dirname(os.path.realpath(__file__)) + "\\clack.wav"
clack = pygame.mixer.Sound(ClackPath)
count = 0
noOfDigits = 3
timeSteps = 10*noOfDigits
class Block:
    def __init__(self,x,y,w,vel,mass):
        self.x = x
        self.y = y
        self.w = w
        self.vel = vel
        self.mass = mass
    def show(self):
        text = Boxfont.render(str(self.mass) + "KG", True, (0,0,0), (200,200,200)) 
        textRect = text.get_rect()
        textRect.center = (self.x + self.w/2, self.y-self.w * 1.25)
        pygame.draw.rect(win,(255,0,0),(self.x,self.y-self.w,self.w,self.w))
        win.blit(text,textRect)
    def update(self):
        self.x += self.vel/100
    def collide(self, other):
        if(self.x + self.w < other.x or self.x > other.x + other.w):
            return False
        else:
            return True
    def rebound(self,other):
        sumMass = self.mass + other.mass
        NewVel = (self.mass-other.mass)/sumMass * self.vel
        NewVel += (2 * other.mass/sumMass) * other.vel
        return NewVel
    def wallCollide(self):
        return self.x <=0
    def reverse(self):
        self.vel *= -1
         

Block1 = Block(math.floor(ScreenWidth/3),math.floor(ScreenHeight/2),25,0,1)
Block2 = Block(math.floor(ScreenWidth*0.75),math.floor(ScreenHeight/2),25*(noOfDigits),-5/timeSteps,100**(noOfDigits-1))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    win.fill((200,200,200))
    win.fill((0,0,0),(0,ScreenHeight/2,ScreenWidth,ScreenHeight/2))
    Clackstext = Countfont.render(str(count), True, (0,0,0), (200,200,200)) 
    textRect = Clackstext.get_rect()
    textRect.center = (ScreenWidth/2, 25)
    win.blit(Clackstext,textRect)
    for i in range(timeSteps):
        if Block1.collide(Block2):
            v1 = Block1.rebound(Block2)
            v2 = Block2.rebound(Block1)
            Block1.vel = v1
            Block2.vel = v2 
            count +=1
            clack.play()
        if Block1.wallCollide():
            Block1.reverse()
            count +=1
            clack.play()
        Block1.update()
        Block2.update()
    Block1.show()
    Block2.show()
    pygame.display.update()
pygame.quit()