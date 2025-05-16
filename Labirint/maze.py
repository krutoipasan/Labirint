#нічого тут й не було, ви повинні мені вірити#
##############################################
from pygame import *
import sys
from PIL import *
mixer.init()

window=display.set_mode((700, 500))
image=image.load
background=transform.scale(image("background.jpg"), (700, 500))
music=mixer.Sound("jungles.ogg")
music.play()

window.blit(background, (0, 0))

class GameSprite():
    def __init__(self, p_image, p_speed, p_x, p_y):
        super().__init__()
        self.image=transform.scale(image(p_image), (50, 50))
        self.speed=p_speed
        self.rect=self.image.get_rect()
        self.x=p_x
        self.y=p_y
    def reset(self):
        window.blit(self.image, (self.x, self.y))

player=GameSprite("hero.png", 10, 50, 250)

FPS=60

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
    GameSprite.reset(player)
    display.update()
