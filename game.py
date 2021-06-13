from scoreText import ScoreText
import arcade
from arcade.key import F
from globals import *
from paddle import Paddle
from ball import Ball
from scoreText import ScoreText

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.left_paddle = Paddle()
        self.right_paddle = Paddle()
        self.ball = Ball()

        self.score_text = ScoreText()

        #Controls
        self.w_pressed = False
        self.s_pressed = False
        self.down_pressed = False
        self.up_pressed = False
        self.d_pressed = False
        self.left_pressed = False

    def setup(self):
        self.left_paddle.is_connected = True

    def on_key_press(self, key, key_modifiers):
        #Player left
        if(key == arcade.key.W):
            self.w_pressed = True
        elif key == arcade.key.S:
            self.s_pressed = True
        if key == arcade.key.D:
            self.d_pressed = True

        #player right
        if(key == arcade.key.UP):
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        if key == arcade.key.LEFT:
            self.left_pressed = True

    def on_key_release(self, symbol: int, modifiers: int):
        if(symbol == arcade.key.W):
            self.w_pressed = False
        elif symbol == arcade.key.S:
            self.s_pressed = False
        if(symbol == arcade.key.UP):
            self.up_pressed = False
        elif symbol == arcade.key.DOWN:
            self.down_pressed = False
        if symbol == arcade.key.D:
            self.d_pressed = False
        if symbol == arcade.key.LEFT:
            self.left_pressed = False

    def on_draw(self):
        arcade.start_render()
        self.left_paddle.draw()
        self.right_paddle.draw(SCREEN_WIDTH-15)
        self.score_text.draw()
        self.score_text.check_victory()
        self.ball.draw()

    def on_update(self, delta_time: float):
        
        if self.ball.x > SCREEN_WIDTH:
            self.left_paddle.is_connected = True
            self.score_text.add_right()
            print(self.left_paddle.is_connected)
        if self.ball.x < 0:
            self.right_paddle.is_connected = True
            self.score_text.add_left()
            print(self.right_paddle.is_connected)


        if(self.left_paddle.is_connected):
            self.left_paddle.connect(self.ball)
        if(self.right_paddle.is_connected):
            self.right_paddle.connect(self.ball)
        if(not self.score_text.is_game_end()):    
            self.left_paddle.move(self.w_pressed, self.s_pressed)
            self.right_paddle.move(self.up_pressed, self.down_pressed)
            if self.d_pressed and self.left_paddle.is_connected:
                self.left_paddle.launchBall(self.ball)
            if self.left_pressed and self.right_paddle.is_connected:
                self.right_paddle.launchBall(self.ball)
            if self.left_paddle.is_connected == False and self.right_paddle.is_connected == False:
                self.ball.move()
    
        self.ball.detect_paddle(self.right_paddle)
        self.ball.detect_paddle(self.left_paddle)
            
def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()
if __name__ == "__main__":
    main()