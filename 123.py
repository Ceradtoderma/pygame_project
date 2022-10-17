import pygame as pg
from pygame.math import Vector2
from pathlib import Path

class Player(pg.sprite.Sprite):

    def __init__(self, x, y, walls):
        super().__init__()
        self.player_img = pg.image.load(Path('img', 'Knight.png'))
        self.image = self.player_img
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=(x, y))
        self.pos = Vector2(x, y)  # Position vector.
        self.vel = Vector2(0, 0)  # Velocity vector.
        self.walls = walls  # A reference to the wall group.

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.vel.y = -3
        elif keys[pg.K_s]:
            self.vel.y = 3
        else:
            self.vel.y = 0
        if keys[pg.K_a]:
            self.vel.x = -3
        elif keys[pg.K_d]:
            self.vel.x = 3
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

    def rotate(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            self.image = pg.transform.rotate(self.player_img, 180)
        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            self.image = self.player_img
        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            self.image = pg.transform.rotate(self.player_img, 90)
        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            self.image = pg.transform.rotate(self.player_img, 270)

class Wall(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('img/wall.png')
        self.image = pg.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()

    all_sprites = pg.sprite.Group()
    walls = pg.sprite.Group()

    x = 200
    y = 100
    for i in range(8):
        w = Wall(x, y)
        walls.add(w)
        all_sprites.add(w)
        x += 40

    for i in range(8):
        w = Wall(x, y)
        walls.add(w)
        all_sprites.add(w)
        y += 40

    player = Player(300, 300, walls)
    all_sprites.add(player)

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

            player.rotate(event)

        all_sprites.update()
        screen.fill((30, 30, 30))
        all_sprites.draw(screen)

        pg.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()