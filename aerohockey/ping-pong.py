from pygame import *
from random import *
import random
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

# оригинал цвета 200 255 255
back = (88, 0, 189)
win_width = 800
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)


game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('roket.png', 30, 200, 4, 150, 150)
racket2 = Player('roket.png', 630, 200, 4, 150, 150)
ball = GameSprite('baller.png', 200, 200, 4, 30, 30)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = randint(3, 10)
speed_y = randint(3, 10)
hw = randint(3, 7)
hh = random.randint(-7, -3)

mixer.init()

mixer.music.load('hockey theme.mp3')
mixer.music.play()
fire = mixer.Sound('jump.ogg')
win = mixer.Sound('applod.ogg')
start = mixer.Sound('whistle.ogg')

score1 = 0
score2 = 0

life_color = (0,255,0)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            

    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        text_score = font.render(str(score1), 4, life_color)
        window.blit(text_score, (700, 10))

        text_score = font.render(str(score2), 4, life_color)
        window.blit(text_score, (100, 10))


        if sprite.collide_rect(racket1, ball): 
            speed_x= hw
            speed_y= randint(3, 10)
            fire.play()
            
        if sprite.collide_rect(racket2, ball):
            speed_x= hh
            speed_y= randint(3, 10)
            fire.play()

        if ball.rect.y > win_height-50 or ball.rect.y <0:
            speed_y *= -1
            fire.play()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (300, 200))
            score1 += 1
            finish = True
            win.play()

            #time.delay(9000)
            #finish = False

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (300, 200))
            score2 += 1
            finish = True
            win.play()

            #time.delay(9000)
            #finish = False
            
        racket1.reset()
        racket2.reset()
        ball.reset()


    if finish == True:
        time.delay(3000)

        start.play()

        racket1 = Player('roket.png', 30, 200, 4, 150, 150)
        racket2 = Player('roket.png', 630, 200, 4, 150, 150)
        ball = GameSprite('baller.png', 200, 200, 4, 30, 30)

        finish = False
        

    display.update()
    clock.tick(FPS)


    