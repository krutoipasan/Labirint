#нічого тут й не було, ви повинні мені вірити#
##############################################
from pygame import *
import sys
from PIL import *
mixer.init()

win_width=700
win_height=500

window=display.set_mode((win_width, win_height))
image=image.load
background=transform.scale(image("background.jpg"), (win_width, win_height))
music=mixer.Sound("jungles.ogg")
music.play()

class GameSprite():
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
        if keys_pressed[K_UP] and self.rect.y < win_height+30:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height-490:
            self.rect.y+=self.speed
        if keys_pressed[K_LEFT] and self.rect.x < win_width+30:
            self.rect.x-=self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width-690:
            self.rect.x+=self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.direction == "right":
            self.rect.x += self.speed
player=Player("hero.png", 5, 50, 250)

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
    GameSprite.reset(player)
    Player.update(player)
    display.update()
    clock.tick(FPS)