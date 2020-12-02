import pygame as pg


class Handler:
    FPS = 60
    screen_width = 800
    screen_height = 600
    display = pg.display.set_mode((screen_width, screen_height))
    up = False
    right = False
    left = False
    space = False
