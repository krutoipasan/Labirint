#нічого тут й не було, ви повинні мені вірити#
##############################################
from pygame import *
import sys
from PIL import *
mixer.init()
font.init()
win_width=700
win_height=500

window=display.set_mode((win_width, win_height))
image=image.load
background=transform.scale(image("background.jpg"), (win_width, win_height))
music=mixer.Sound("jungles.ogg")
music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_speed, p_x, p_y):
        super().__init__()
        self.image=transform.scale(image(p_image), (50, 50))
        self.speed=p_speed
        self.rect=self.image.get_rect()
        self.rect.x=p_x
        self.rect.y=p_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= (win_height-500):
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= (win_height-50):
            self.rect.y+=self.speed
        if keys_pressed[K_LEFT] and self.rect.x >= (win_width-700):
            self.rect.x-=self.speed
        if keys_pressed[K_RIGHT] and self.rect.x <= (win_width-50):
            self.rect.x+=self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 520:
            self.direction = "right"
        if self.rect.x >= 650:
            self.direction = "left"
        if self.direction == "right":
            self.rect.x += self.speed
        if self.direction == "left":
            self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, width, height, wall_x, wall_y, red, green, blue):
        super().__init__()
        self.width=width
        self.height=height
        self.image=Surface((width, height))
        self.red=red
        self.green=green
        self.blue=blue
        self.image.fill((red, green, blue))
        self.rect=self.image.get_rect()
        self.rect.x=wall_x
        self.rect.y=wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Treasure(sprite.Sprite):
    def __init__(self, tr_image, tr_x, tr_y):
        self.tr_image=transform.scale(image(tr_image), (50, 50))
        self.rect=self.tr_image.get_rect()
        self.rect.x=tr_x
        self.rect.y=tr_y
    def reset(self):
        window.blit(self.tr_image, (self.rect.x, self.rect.y))



player=Player("hero.png", 5, 50, 250)
enemy=Enemy("cyborg.png", 2, 650, 250)
wall1=Wall(20, 400, 500, 100, 50, 50, 255)
wall2=Wall(150, 20, 215, 100, 50, 50, 255)
wall3=Wall(150, 20, 215, 300, 50, 50, 255)
wall4=Wall(20, 400, 120, 100, 50, 50, 255)
wall5=Wall(20, 430, 280, 0, 50, 50, 255)
wall6=Wall(20, 400, 420, 0, 50, 50, 255)
wall7=Wall(80, 20, 360, 200, 50, 50, 255)
wall8=Wall(80, 20, 120, 200, 50, 50, 255)
treasure=Treasure("treasure.png", 580, 450)
FPS=60
clock=time.Clock()
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
    window.blit(background, (0, 0))
    if finish == True:
        time.wait(2000)
        break
    if finish != True:
        GameSprite.reset(player)
        GameSprite.reset(enemy)
        Treasure.reset(treasure)
        Player.update(player)
        Enemy.update(enemy)
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
    if player.rect.colliderect(enemy.rect) or player.rect.colliderect(wall1) or player.rect.colliderect(wall2) or player.rect.colliderect(wall3) or player.rect.colliderect(wall4) or player.rect.colliderect(wall5):
        fontdefeat=font.SysFont(None, 140)
        textdefeat=fontdefeat.render("YOU LOSE!", 1, (200, 0, 0))
        window.blit(textdefeat, (90, 200))
        sounddefeat=mixer.Sound("kick.ogg")
        sounddefeat.play()
        finish = True
    if player.rect.colliderect(treasure.rect):
        fontvictory=font.SysFont(None, 140)
        textvictory=fontvictory.render("YOU WIN!", 1, (200, 200, 0))
        window.blit(textvictory, (110, 200))
        soundvictory=mixer.Sound("money.ogg")
        soundvictory.play()
        finish = True
    display.update()
    clock.tick(FPS)