from sprites import Wall
from conf import *


def generate_walls(pop=None):
    walls = []
    x = y = 0
    wall_side = Wall(x, y).rect.width
    horizontal_walls = WIDTH/wall_side - 1
    vertical_walls = HEIGHT / wall_side - 1
    direction = {'right': (wall_side, 0, horizontal_walls),
                 'down': (0, wall_side, vertical_walls),
                 'left': (-wall_side, 0, horizontal_walls),
                 'up': (0, -wall_side, vertical_walls)}
    for move in direction:
        count = 0
        while count != direction[move][2]:
            walls.append(Wall(x, y))
            x += direction[move][0]
            y += direction[move][1]
            count += 1
    if pop:
        del walls[pop[0]:pop[1]]
    return walls


def generate_walls2(walls, all_sprites):
    x = y = 0
    width_wall = Wall(x, y).rect.width
    nums_walls_x = int(WIDTH / width_wall)
    y_up = 0
    y_down = HEIGHT - width_wall
    for i in range(nums_walls_x):
        w = Wall(x, y_up)
        walls.add(w)
        all_sprites.add(w)
        w = Wall(x, y_down)
        walls.add(w)
        all_sprites.add(w)
        x += w.rect.width
    x_left = 0
    x_right = WIDTH - width_wall
    y = 0
    for i in range(int(HEIGHT / width_wall)):
        w = Wall(x_left, y)
        walls.add(w)
        all_sprites.add(w)
        w = Wall(x_right, y)
        walls.add(w)
        all_sprites.add(w)
        y += w.rect.width

print(generate_walls())