import pygame as pg
import random
from enum import Enum
from collections import namedtuple

pg.init()

# Setting up font
font = pg.font.SysFont('arial', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

#Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)


BODY_SIZE = 20
SPEED = 10
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
        # get user input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pg.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pg.K_UP:
                    self.direction = Direction.UP
                elif event.key == pg.K_DOWN:
                    self.direction = Direction.DOWN

        # move snake
        self._move(self.direction) #update the head
        self.snake.insert(0, self.head)

        # check if boundary is hit
        if self._boundary_hit():
            game_over = True
            return game_over, self.score
        # check if game ends
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score
        # place new food or move snake
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()
        # update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        # return game over and score
        return game_over, self.score

        # making the snake jump to the other side of the screen
    def _boundary_hit(self):
        # checking if the snake hits the boundary
        if self.head.x > self.w - BODY_SIZE or self.head.x < 0 or self.head.y > self.h - BODY_SIZE or self.head.y < 0:
            return True

    def _is_collision(self):
        # checking if the snake hits itself
        if self.head in self.snake[1:]:
            return True
        
        return False

    def _update_ui(self):
        self.display.fill(BLACK)

        #Draw the snake
        for p in self.snake:
            rncolor1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            rncolor2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            pg.draw.rect(self.display, rncolor1, pg.Rect(p.x, p.y, BODY_SIZE, BODY_SIZE))
            pg.draw.rect(self.display, rncolor2, pg.Rect(p.x + 4, p.y + 4, 12, 12))

        pg.draw.rect(self.display, RED, pg.Rect(self.food.x, self.food.y, BODY_SIZE, BODY_SIZE))

        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pg.display.flip()

    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BODY_SIZE
        elif direction == Direction.LEFT:
            x -= BODY_SIZE
        elif direction == Direction.DOWN:
            y += BODY_SIZE
        elif direction == Direction.UP:
            y -= BODY_SIZE

        self.head = Point(x, y)


if __name__ == '__main__':
    game = Snake()

    #Loop of the game
    while True:
        game_over, score = game.play_step()

        if game_over == True:
            break

    print('Final score', score)


    pg.quit()