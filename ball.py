from globals import SCREEN_HEIGHT, SCREEN_WIDTH
import arcade
import random
class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xDir = 3
        self.yDir = 3
        self.radius = 5
        self.color = arcade.color.WHITE
        self.detected_paddle = False
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)
    def hit_paddle(self,paddle):
        return self.y > paddle.bottom and self.y < paddle.top and self.x >= paddle.x - paddle.width/2 and self.x <= paddle.x + paddle.width/2
    def move(self):
        #victor Left
        if self.x > SCREEN_WIDTH:
            pass
        #victor right
        if self.x < 0:
            pass
        if self.y > SCREEN_HEIGHT or self.y < 0:
            self.yDir *= -1
        self.x += self.xDir
        self.y += self.yDir
    def detect_paddle(self, paddle):
        if self.hit_paddle(paddle):
            self.xDir *= -1
            self.detected_paddle = True
            # print(self.detected_paddle, paddle.bottom, paddle.top)
        else:
            self.detected_paddle = False

