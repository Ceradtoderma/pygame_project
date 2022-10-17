import pygame as pg
from pygame.math import Vector2
from pathlib import Path
from conf import *
from sg.hero import Paladin
from sg.enemy import Rat as Rat_log
from sg.weapons import Sword as Sword_log

class Player(pg.sprite.Sprite):

    def __init__(self, x, y, walls):
        super().__init__()
        self.logic = Paladin()
        self.player_img = pg.image.load(Path('img', 'Knight.png'))
        self.image = self.player_img
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=(x, y))
        self.pos = Vector2(x, y)  # Position vector.
        self.vel = Vector2(0, 0)  # Velocity vector.
        self.walls = walls  # A reference to the wall group.

    def update(self):
        self.rotate()
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.vel.y = -8
        elif keys[pg.K_s]:
            self.vel.y = 8
        else:
            self.vel.y = 0
        if keys[pg.K_a]:
            self.vel.x = -8
        elif keys[pg.K_d]:
            self.vel.x = 8
        else:
            self.vel.x = 0
        self.pos += self.vel
        self.wall_collisions()

    def wall_collisions(self):
        """Handle collisions with walls."""
        self.rect.centerx = self.pos.x
        for wall in pg.sprite.spritecollide(self, self.walls, False):
            if self.vel.x > 0:
                self.rect.right = wall.rect.left
            elif self.vel.x < 0:
                self.rect.left = wall.rect.right
            self.pos.x = self.rect.centerx

        self.rect.centery = self.pos.y
        for wall in pg.sprite.spritecollide(self, self.walls, False):
            if self.vel.y > 0:
                self.rect.bottom = wall.rect.top
            elif self.vel.y < 0:
                self.rect.top = wall.rect.bottom
            self.pos.y = self.rect.centery

    def rotate(self):
        if self.vel.y < 0:
            if self.vel.x == 0:
                self.image = self.player_img
            elif self.vel.x > 0:
                self.image = pg.transform.rotate(self.player_img, 315)
            elif self.vel.x < 0:
                self.image = pg.transform.rotate(self.player_img, 45)
        if self.vel.y > 0:
            if self.vel.x == 0:
                self.image = pg.transform.rotate(self.player_img, 180)
            elif self.vel.x > 0:
                self.image = pg.transform.rotate(self.player_img, 225)
            elif self.vel.x < 0:
                self.image = pg.transform.rotate(self.player_img, 135)
        if self.vel.y == 0:
            if self.vel.x > 0:
                self.image = pg.transform.rotate(self.player_img, 270)
            elif self.vel.x < 0:
                self.image = pg.transform.rotate(self.player_img, 90)


class Wall(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('img/wall.png')
        self.image = pg.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Rat(pg.sprite.Sprite):
    def __init__(self, center):
        pg.sprite.Sprite.__init__(self)
        self.logic = Rat_log()
        self.image = pg.image.load('img/ratpng.png')
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.speedx *= -1
        if self.rect.left < 0:
            self.speedx *= -1
        if self.rect.top < 0:
            self.speedy *= -1
        if self.rect.bottom > HEIGHT:
            self.speedy *= -1



class Sword(pg.sprite.Sprite):
    def __init__(self, center):
        pg.sprite.Sprite.__init__(self)
        self.logic = Sword_log()
        self.image = pg.image.load('img/sword.png')
        self.rect = self.image.get_rect()
        self.rect.center = center