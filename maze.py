#нічого тут й не було, ви повинні мені вірити#
##############################################
from pygame import *
import sys
from PIL import *
mixer.init()
font.init()
win_width=1000
win_height=500

window=display.set_mode((win_width, win_height))
image=image.load
background=transform.scale(image("jungle.jpg"), (win_width, win_height))
music=mixer.Sound("jungles.ogg")
music.play()
coins_collected=0

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
        if keys_pressed[K_LEFT] and self.rect.x >= (win_width-1000):
            self.rect.x-=self.speed
        if keys_pressed[K_RIGHT] and self.rect.x <= (win_width-50):
            self.rect.x+=self.speed
        if keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]:
            self.speed=2
        else:
            self.speed=5
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
    def chase(self):
        if self.rect.x <= player.rect.x:
            self.x_direction = "right"
        if self.rect.x >= player.rect.x:
            self.x_direction = "left"
        if self.rect.y <= player.rect.y:
            self.y_direction = "up"
        if self.rect.y >= player.rect.y:
            self.y_direction = "down"
        
        if self.x_direction == "right":
            self.rect.x += self.speed
        if self.x_direction == "left":
            self.rect.x -= self.speed
        if self.y_direction == "up":
            self.rect.y += self.speed
        if self.y_direction == "down":
            self.rect.y -= self.speed
class Wall(sprite.Sprite):
    def __init__(self, w_image, width, height, wall_x, wall_y):
        super().__init__()
        self.width=width
        self.height=height
        self.image=transform.scale(image(w_image), (width, height))
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

class Coin(sprite.Sprite):
    def __init__(self, c_image, c_x, c_y):
        self.c_image=transform.scale(image(c_image), (35, 35))
        self.rect=self.c_image.get_rect()
        self.rect.x=c_x
        self.rect.y=c_y
    def reset(self):
        window.blit(self.c_image, (self.rect.x, self.rect.y))
    def collected(self):
        global coins_collected
        self.rect.x=1500
        coins_collected+=1

player=Player("pirate.png", 5, 50, 250)
enemy=Enemy("gorilla.png", 2, 650, 250)
wall1=Wall("wall.jpg", 20, 400, 500, 100)
wall2=Wall("wall.jpg", 150, 20, 215, 100)
wall3=Wall("wall.jpg", 150, 20, 215, 300)
wall4=Wall("wall.jpg", 20, 400, 120, 100)
wall5=Wall("wall.jpg", 20, 430, 280, 0)
wall6=Wall("wall.jpg", 20, 400, 420, 0)
wall7=Wall("wall.jpg", 80, 20, 360, 200)
wall8=Wall("wall.jpg", 80, 20, 120, 200)
treasure=Treasure("treasure_chest.png", 800, 450)
coin1=Coin("coin.png", 50, 450)
coin2=Coin("coin.png", 320, 35)
coin3=Coin("coin.png", 950, 15)

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
    if finish != True:
        GameSprite.reset(player)
        GameSprite.reset(enemy)
        Player.update(player)
        if player.rect.x >= 500:
            Enemy.chase(enemy)
        else:
            Enemy.update(enemy)
        coin1.reset()
        coin2.reset()
        coin3.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        if coins_collected <= 3:
            fontinstr=font.SysFont(None, 20)
            textinstr=fontinstr.render("Зберіть усі монети, щоб відкрити скарб!"), 1, (255, 255, 255)
            window.blit(textinstr, (0, 0))
    else:
        time.wait(2500)
        break
    if player.rect.colliderect(enemy.rect) or player.rect.colliderect(wall1) or player.rect.colliderect(wall2) or player.rect.colliderect(wall3) or player.rect.colliderect(wall4) or player.rect.colliderect(wall5):
        fontdefeat=font.SysFont(None, 140)
        textdefeat=fontdefeat.render("YOU LOSE!", 1, (200, 0, 0))
        window.blit(textdefeat, (240, 200))
        sounddefeat=mixer.Sound("kick.ogg")
        sounddefeat.play()
        finish = True

    if player.rect.colliderect(coin1.rect):
        coin1.collected()
        soundcoin=mixer.Sound("coin-pick-up.mp3")
        soundcoin.play()
    if player.rect.colliderect(coin2.rect):
        coin2.collected()
        soundcoin=mixer.Sound("coin-pick-up.mp3")
        soundcoin.play()
    if player.rect.colliderect(coin3.rect):
        coin3.collected()
        soundcoin=mixer.Sound("coin-pick-up.mp3")
        soundcoin.play()

    if coins_collected==3:
        soundtropen=mixer.Sound("treasure-unlocked.mp3")
        soundtropen.play()
        coins_collected+=1
    if coins_collected>=4:
        Treasure.reset(treasure)
        if player.rect.colliderect(treasure.rect):
            fontvictory=font.SysFont(None, 140)
            textvictory=fontvictory.render("YOU WIN!", 1, (200, 200, 0))
            window.blit(textvictory, (270, 200))
            soundvictory=mixer.Sound("money.ogg")
            soundvictory.play()
            finish = True
    display.update()
    clock.tick(FPS)