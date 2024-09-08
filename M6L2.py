import pygame
from pygame import *

clock = time.Clock()

image_ball = "ball.png"
image_bg = "background.png"


main_win = pygame.display.set_mode((600, 500))
background = transform.scale(image.load(image_bg), (600, 500))

class Ball(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))
class Player(Ball):
    def player_1(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y  -=self.speed

        if keys[K_s]:
            self.rect.y  +=self.speed


    def player_2(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y  -=self.speed

        if keys[K_DOWN]:
            self.rect.y  +=self.speed

ball = Ball(image_ball, 200, 200, 5, 50, 50 )
player_1 = Player('player1.png', 30, 200, 4, 50, 150)
player_2 = Player('player2.png', 520, 200, 4, 50, 150)

finish = False
game = True
speed_x , speed_y = 3, 3
font.init()
font = font.Font(None, 35)
lose1 = font.render("PLAYER 1 LOSE", True, (0,153,0))
lose2 = font.render("PLAYER 2 LOSE", True, (0,0,153))
while game:
    for e in event.get():
        if e.type  == QUIT:
            game = False
    if finish != True:
        main_win.blit(background, (0,0))
        player_1.player_1()
        player_2.player_2()

        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if ball.rect.y > 500 - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            speed_x *= -1


        if ball.rect.x < 0:
            main_win.blit(lose1, (200,200))
            finish = True

        if ball.rect.x > 600:
            main_win.blit(lose2, (200,200))
            finish = True

        player_1.reset()
        player_2.reset()
        ball.reset()
    display.update()
    clock.tick(40)



