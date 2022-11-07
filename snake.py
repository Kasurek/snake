import pygame as pg
import random
from enum import Enum
from collections import namedtuple

pg.init()

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

BODY_SIZE = 20
class Snake:

    def __init__(self,w=640,h=480):
        self.w = w
        self.h = h

        # init display
        self.display = pg.display.set_mode((self.w, self.h))
        pg.display.set_caption('Snake')
        self.clock = pg.time.Clock()
        
        # init game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head,
                     Point(self.head.x-BODY_SIZE, self.head.y),
                     Point(self.head.x-(2*BODY_SIZE), self.head.y)]

        self.score = 0
        self.food = None
        self._place_food()

    def _place_food(self):
        x = random.randint(0, (self.w-BODY_SIZE) // BODY_SIZE) * BODY_SIZE
        y = random.randint(0, (self.h-BODY_SIZE) // BODY_SIZE) * BODY_SIZE
        self.food = Point(x,y)
        if self.food in self.snake:
            self._place_food()


    def play_step(self):
        # 1. get user input

        # 2. move snake

        # 3. check if game ends

        # 4. place new food or move snake

        # 5. update ui and clock

        # 6. return game over and score
        game_over = False
        return game_over, self.score


if __name__ == '__main__':
    game = Snake()

    #Loop of the game
    while True:
        game_over, score = game.play_step()

        if game_over == True:
            break

    print('Final score', score)


    pg.quit()