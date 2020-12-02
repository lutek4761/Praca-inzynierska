from pygame.locals import *
import pygame as pg
from handler import Handler
from game import Game

pg.init()
pg.font.init()
delta = 0
clock = pg.time.Clock()
game = Game()

while True:
    delta += clock.tick()
    if delta > 1000 / Handler.FPS:
        delta -= 1000 / Handler.FPS
    else:
        continue

    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pg.quit()
            exit(0)

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                Handler.space = True
            if event.key == pg.K_UP:
                Handler.up = True
            if event.key == pg.K_RIGHT:
                Handler.right = True
            if event.key == pg.K_LEFT:
                Handler.left = True

        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                Handler.space = False
            if event.key == pg.K_UP:
                Handler.up = False
            if event.key == pg.K_RIGHT:
                Handler.right = False
            if event.key == pg.K_LEFT:
                Handler.left = False
    game.erase()
    game.tick()
    game.render()
    pg.display.update()
