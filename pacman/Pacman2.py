# Nashawn Longmire
# Pygame
# Ultimate Bridge Task
import pygame
import random
import time

WIDTH = 950
HEIGHT = 950
FPS = 60# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 52)
YELLOW = (255, 255, 0)
GRAY = (95,95,95)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reverse Pacman")
clock = pygame.time.Clock()
introSound = pygame.mixer.music.load("Green Hill Zone.ogg")
background = pygame.image.load("Pmap.png")
pacman = pygame.image.load('pacman.png')
baddie = pygame.image.load('Ghost.png')
pacman.set_colorkey(BLACK)
deathSound = pygame.mixer.Sound("Death.ogg")
pacman.convert_alpha()
pygame.mixer.music.play(-1)

def game_loop():
    class Pacman(pygame.sprite.Sprite):
        def __init__(self):
            x = 200
            y = 485
            pygame.sprite.Sprite.__init__(self)
            self.image = pacman
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.radius = 25
            self.rect.centerx = x
            self.rect.bottom = y
            self.speed = 14
            #z = pygame.draw.circle(self.image, RED,self.rect.center, self.radius)
        def setX(self):
            self.rect.x = 200
        def getX(self):
            return (self.rect.x)
        def getY(self):
            return self.rect.y
        def setY(self):
            self.rect.y = 485
        def update(self):
            a = self.checkController()
            if (a[0] == 1):
                self.rect.x += self.speed
            elif (a[0] == -1):
                self.rect.x -= self.speed
            elif (a[1] == 1):
                self.rect.y -= self.speed
            elif (a[1] == -1):
                self.rect.y += self.speed
                
            
        def checkController(self):
            clock = pygame.time.Clock()
            pygame.joystick.init()
            for j in range(3):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                joystick = pygame.joystick.Joystick(0)
                joystick.init()
                hats = joystick.get_numhats()
                for i in range(hats):
                    hat = joystick.get_hat(i)
                    if (j == 2):
                        return hat
                clock.tick(60)
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            pygame.sprite.Sprite.__init__(self)
            self.image = baddie
            self.rect = self.image.get_rect()
            self.radius = (self.rect.width * .85 / 2)
            #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.x = 500
            self.rect.y = 450
            self.speed = 13
        def setX(self):
            self.rect.x = 500
        def setY(self):
            self.rect.y = 450
        def getX(self):
            return (self.rect.x)
        def getY(self):
            return self.rect.y
        def checkController(self):
            clock = pygame.time.Clock()
            pygame.joystick.init()

            for j in range(3):
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        done = True
                joystick = pygame.joystick.Joystick(1)
                joystick.init()
                hats = joystick.get_numhats()
                for i in range(hats):
                    hat = joystick.get_hat(i)
                    if (j == 2):
                        return hat
                clock.tick(60)
            
        def update(self):
            a = self.checkController()
            print(a)
            if (a[0] == 1):
                self.rect.x += self.speed
            elif (a[0] == -1):
                self.rect.x -= self.speed
            elif (a[1] == 1):
                self.rect.y -= self.speed
            elif (a[1] == -1):
                self.rect.y += self.speed


    class Enemy2(pygame.sprite.Sprite):
            def __init__(self):
                #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
                pygame.sprite.Sprite.__init__(self)
                self.image = baddie
                self.rect = self.image.get_rect()
                self.radius = (self.rect.width * .85 / 2)
                #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
                self.rect.x = 450
                self.rect.y = 450
                self.speed = 13
            def setX(self):
                self.rect.x = 450
            def setY(self):
                self.rect.y = 450
            def getX(self):
                return (self.rect.x)
            def getY(self):
                return self.rect.y
            def checkController(self):
                clock = pygame.time.Clock()
                pygame.joystick.init()

                for j in range(3):
                    for event in pygame.event.get(): 
                        if event.type == pygame.QUIT: 
                            done = True
                    joystick = pygame.joystick.Joystick(2)
                    joystick.init()
                    hats = joystick.get_numhats()
                    for i in range(hats):
                        hat = joystick.get_hat(i)
                        if (j == 2):
                            return hat
                    clock.tick(60)
                
            def update(self):
                a = self.checkController()
                if (a[0] == 1):
                    self.rect.x += self.speed
                elif (a[0] == -1):
                    self.rect.x -= self.speed
                elif (a[1] == 1):
                    self.rect.y -= self.speed
                elif (a[1] == -1):
                    self.rect.y += self.speed

            

        
                 
    all_sprites = pygame.sprite.Group()
    player = Pacman()
    ghost = Enemy()
    ghost2 = Enemy2()
    all_sprites.add(player)
    all_sprites.add(ghost)
    all_sprites.add(ghost2)
    total = 0
    #for i in range(5):
        #m = Enemy()
        #all_sprites.add(m)
        #enemy.add(m)
    
    running = True
    range1 = 15
    while running:
        total = total + 1
        screen.blit(background,(0,0))
        time = pygame.time.get_ticks()
            
        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
        # Update
        if ((abs(player.getX() - ghost.getX()) <= range1) and (abs(player.getY() - ghost.getY()) <= range1)) or ((abs(player.getX() - ghost2.getX()) <= range1) and (abs(player.getY() - ghost2.getY()) <= range1)):
            player.setX()
            player.setY()
            ghost.setX()
            ghost.setY()
            ghost2.setX()
            ghost2.setY()
            deathSound.play()
            
            
        all_sprites.update()

        # Draw / render
        all_sprites.draw(screen)
        
            
        pygame.display.update()

game_loop()
pygame.quit()
quit()




        
            
            
            


