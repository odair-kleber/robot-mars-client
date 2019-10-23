import cursors
import directions

BOUNDS = 5
plain = []


def init_plain():
    for _ in range(0, BOUNDS):
        temp = []
        for _ in range(0, BOUNDS):
            temp.append(" \u25a2 ")
        plain.append(temp)


def print_ground():
    for x in plain:
        for y in x:
            print(y, end='')
        print()


def set_robot_position(x, y, direction):
    if direction == directions.NORTH:
        plain[x][y] = cursors.UP
    elif direction == directions.SOUTH:
        plain[x][y] = cursors.DOWN
    elif direction == directions.EAST:
        plain[x][y] = cursors.RIGHT
    elif direction == directions.WEST:
        plain[x][y] = cursors.LEFT
