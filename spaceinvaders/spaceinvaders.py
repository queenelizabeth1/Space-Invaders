#dont be overconfident. the game gets gradually faster

from email.base64mime import header_length
import pygame
from pygame.locals import *
from tkinter import *

root = Tk()
root.geometry('500x500')
score = 0

# 2 - Initialize the game
pygame.init()
screen = pygame.display.set_mode((600,600))
bg_img = pygame.image.load('blackhole.jpg')
bg_img = pygame.transform. scale(bg_img,(600,600))

n = 1 
playerbullets = []
pygame.init()


class Ship:
    def __init__(self,x,y,image_name, length, width):
        self.x = x
        self.y = y
        self.pos = [self.x,self.y]
        self.image = pygame.image.load(image_name)
        self.image = pygame.transform.scale(self.image,(length, width))
        self.health = 10
        self.mask = pygame.mask.from_surface(self.image)
    def move_to(self,x,y):
        self.x = x
        self.y = y
        self.draw()
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    def shoot(self, bullets):
        laser = Laser(self.x, self.y)
        bullets.append(laser)
pygame.display.set_caption('Space Invaders')
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 40)

# render text


class Laser:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("laser.jpeg")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.mask = pygame.mask.from_surface(self.image)
    def move(self,x,y):
        self.x = x
        self.y = y
    def draw(self, m):
        screen.blit(self.image, (self.x, self.y))
        self.y -= m
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None   
player = Ship(200,500,"cow.png",100,100)
enemigos = []
def spawn():
    enemyx = -25
    enemyy = 50
    while enemyx <= 425:
        enemyx += 75
        antagonist = Ship(enemyx, enemyy, "viola.png", 75,75)
        enemigos.append(antagonist)
meow = True
times = 0
bark = 0
n = 500
spawn()
recoil = 0
label = myfont.render("Score :" + str(score), 1, (255,255,0))
label2 = myfont.render("Health :" + str(player.health), 1, (255,255,0))

while meow:
    recoil += 1
    screen.blit(bg_img,(0,0)) #set up background
    player.draw() #put character on the screen
    screen.blit(label, (25, 25))
    screen.blit(label2, (250, 25))
    for bullet in playerbullets:  #draw the bullets being shot
        bullet.draw(1)
        for enemy in enemigos:
            if collide(enemy, bullet): #if bullet collides with enemy
                playerbullets.remove(bullet) #destroy bullet
                enemigos.remove(enemy) #destroy enemy
                score += 1
                label = myfont.render("Score :" + str(score), 1, (255,255,0))
                screen.blit(label, (25, 25))
    for event in pygame.event.get(): #end game if x button pressed
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'): #move left
                player.move_to(player.x - 25, player.y)
            if event.key == pygame.K_RIGHT or event.key == ord('d'): #move right
                player.move_to(player.x + 25, player.y)   
            if (event.key == pygame.K_UP) and (recoil > 250): #shoot
                player.shoot(playerbullets)
                recoil = 0
    for enemy in enemigos: #draw enemies
        enemy.draw()
    bark += 1
    if bark > 1500+n:
        spawn()
        bark = 0
    if times > n: #move enemies downwards constantly
        for enemy_ in enemigos:
            enemy_.y += 30
            times = 0
        if n > 500:
            n -= 100
    times += 1
    pygame.display.update()
    for enemy__ in enemigos: #decrease player health if enemy collides with player
        if collide(player, enemy__):
            player.health -= 1
            label2 = myfont.render("Health :" + str(player.health), 1, (255,255,0))
            enemigos.remove(enemy__)
        if enemy__.y > 600:
            player.health -= 1
            enemigos.remove(enemy__)
    if player.health <= 0:
        enemigos = []
        pygame.display.update()
        meow = False
    pygame.display.update()
times = 0
screen.fill((0,0,0))
pygame.display.update()
meow = True
while meow:
    screen.fill((0,0,0))
    label = myfont.render("Game Over.", 1, (255,255,0))
    screen.blit(label, (170,150))
    label3 = myfont.render("Press Down Key to Quit.",1,(255,255,0))
    screen.blit(label3, (26,250))
    pygame.display.update()
    for event in pygame.event.get(): #end game if x button pressed
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_DOWN):
                pygame.quit()


       


