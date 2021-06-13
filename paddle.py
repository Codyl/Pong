from globals import SCREEN_HEIGHT, SCREEN_WIDTH
import arcade
import random
class Paddle:
    def __init__(self):
        self.x = 15
        self.y = SCREEN_HEIGHT/2
        self.width = 15
        self.height = 100
        self.speed = 8
        self.color = arcade.color.WHITE
        self.top = self.y + self.height/2
        self.bottom = self.y - self.height/2
        self.is_connected = False

    def draw(self, x = 15):
        self.x = x
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)
    def moveUp(self):
        self.y += self.speed
        self.top = self.y + self.height/2
        self.bottom = self.y - self.height/2
    def moveDown(self):
        self.y -= self.speed
        self.top = self.y + self.height/2
        self.bottom = self.y - self.height/2
    def move(self, up_pressed, down_pressed):
        if up_pressed and not down_pressed:
            if self.top < SCREEN_HEIGHT:
                self.moveUp()
        if down_pressed and not up_pressed:
            if self.bottom > 0:
                self.moveDown()
    def connect(self, ball):
        ball.xDir = 0
        ball.yDir = 0
        if(self.x == 15):
            ball.x = self.x + 20
        else:
            ball.x = self.x - 20
        ball.y = self.y
    def launchBall(self,ball):
        self.is_connected = False
        if(self.x == 15):
            ball.xDir = 12 + random.random()
        else:
            ball.xDir = -12 + random.random()