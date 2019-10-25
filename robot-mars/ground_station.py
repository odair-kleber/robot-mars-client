import cursors
import directions

_BOUNDS = 5
_plain = []

last_pos_x = 0
last_pos_y = 0
last_dir = directions.NORTH


def init_station():
    _init_plain()
    _set_robot_position(0, 0, directions.NORTH)


def print_ground():
    for x in _plain:
        for y in x:
            print(y, end='')
        print()


def mov_robot():
    pass
    # todo: to implement api


def set_robot_direction(direction):
    _set_robot_position(last_pos_x, last_pos_y, direction)
    # todo: to implement api request


def _init_plain():
    for _ in range(0, _BOUNDS):
        temp = []
        for _ in range(0, _BOUNDS):
            # temp.append(" \u25a2 ")
            temp.append(" \u25a2 ")
        _plain.append(temp)


def _set_robot_position(x, y, direction):
    if direction == directions.NORTH:
        _plain[x][y] = cursors.UP
    elif direction == directions.SOUTH:
        _plain[x][y] = cursors.DOWN
    elif direction == directions.EAST:
        _plain[x][y] = cursors.RIGHT
    elif direction == directions.WEST:
        _plain[x][y] = cursors.LEFT

    last_pos_x = x
    last_pos_y = y
    last_dir = direction

# def move_robot():
