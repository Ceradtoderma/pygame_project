# Pygame шаблон - скелет для нового проекта Pygame
import random

import pygame as pg

from sg.gui_class import Fight
from sprites import Player, Rat, Wall, Sword
from conf import *
from func import generate_walls


# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# Создаем игру и окно
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()
all_sprites = pg.sprite.Group()
walls = pg.sprite.Group()
mobs = pg.sprite.Group()
player = Player(100, 150, walls)
stuff = pg.sprite.Group()

for i in range(5):
    pos_mob = random.randint(20, 300), random.randint(20, 400)
    r = Rat(pos_mob)
    mobs.add(r)
    all_sprites.add(r)
all_sprites.add(player)

sword = Sword((300, 300))
stuff.add(sword)
walls.add(generate_walls((10, 15)))
all_sprites.add(walls, stuff)

background = pg.image.load('img/background.png')
background_rect = background.get_rect()

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        # player.rotate(event)

    # Обновление
    all_sprites.update()
    hits = pg.sprite.spritecollide(player, mobs, True)
    if hits:
        for hit in hits:
            Fight(player.logic, hit.logic).show()
    hits = pg.sprite.spritecollide(player, stuff, True)
    if hits:
        for hit in hits:
            player.logic.weapons.append(hit.logic)
    # Рендеринг
    screen.blit(background, background_rect)

    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pg.display.flip()

pg.quit()
