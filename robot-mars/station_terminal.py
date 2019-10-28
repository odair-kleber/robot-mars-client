import keyboard

import directions
import ground_station


def init_terminal():
    ground_station.init_station()
    ground_station.print_ground()
    keyboard.hook(__check_pressed_key)
    keyboard.wait()


def __check_pressed_key(key):
    __process_direction()


def __process_movement():
    # todo: to implemets...
    pass


def __process_direction():
    try:
        direction = __get_direction()
        if direction is not None:
            __clear()
            ground_station.set_robot_direction(direction)
            ground_station.print_ground()
    except Exception as ex:
        print('Unespected error: ', ex)


def __get_direction():
    if keyboard.is_pressed('right'):
        return directions.EAST
    elif keyboard.is_pressed('left'):
        return directions.WEST
    elif keyboard.is_pressed('down'):
        return directions.SOUTH
    elif keyboard.is_pressed('up'):
        return directions.NORTH


def __clear():
    print('\n' * 100)