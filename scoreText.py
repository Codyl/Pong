import arcade
from globals import *
class ScoreText:
    def __init__(self):
        self.right_score = 0
        self.left_score = 0
    def draw(self):
        if(self.left_score >= 10):
                arcade.draw_text(str(self.left_score), SCREEN_WIDTH/2-45, SCREEN_HEIGHT - 80, arcade.color.WHITE, 40)
        else:
            arcade.draw_text(str(self.left_score), SCREEN_WIDTH/2-20, SCREEN_HEIGHT - 80, arcade.color.WHITE, 40)
        arcade.draw_text(":", SCREEN_WIDTH/2+5, SCREEN_HEIGHT - 75, arcade.color.WHITE, 40)
        arcade.draw_text(str(self.right_score), SCREEN_WIDTH/2+20, SCREEN_HEIGHT - 80, arcade.color.WHITE, 40)
    def add_right(self):
        self.right_score+=1
    def add_left(self):
        self.left_score+=1
    def check_victory(self):
        if(self.right_score == WINNING_SCORE):
            arcade.draw_text("Right Victory", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.WHITE, 60)
        if(self.left_score == WINNING_SCORE):
            arcade.draw_text("Left Victory", 0, SCREEN_HEIGHT/2, arcade.color.WHITE, 60)
    def is_game_end(self):
        return (self.left_score == WINNING_SCORE or self.right_score == WINNING_SCORE)
        