import os
import time

import keyboard

import directions
import ground_station


def init_terminal():
    __log_start()
    ground_station.init_station()
    ground_station.print_ground()
    keyboard.hook(__check_pressed_key)
    keyboard.wait('esc')
    __log_finish()


def __log_start():
    __clear()
    print('Connecting with mars station...')
    time.sleep(2)
    __clear()


def __log_finish():
    __clear()
    print('Mars station was disconnected')


def __check_pressed_key(key):
    __process_movement()
    __process_direction()


def __process_movement():
    try:
        if __requested_movement():
            __clear()
            ground_station.mov_robot()
            ground_station.print_ground()
    except Exception as ex:
        print('Unespected error: ', ex)


def __requested_movement() -> bool:
    return keyboard.is_pressed('shift')


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
    os.system('cls' if os.name == 'nt' else 'clear')
