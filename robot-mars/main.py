import ground_station
import keyboard
import directions

def check_pressed_key(key):
    try:
        direction = _get_direction()
        if dir is not None:
            _clear()
            ground_station.set_robot_direction(direction)
            ground_station.print_ground()
    except Exception as ex:
        print('Unespected error: ', ex)


def _get_direction():
    if keyboard.is_pressed('right'):
        return directions.EAST
    elif keyboard.is_pressed('left'):
        return directions.WEST
    elif keyboard.is_pressed('down'):
        return directions.SOUTH
    elif keyboard.is_pressed('up'):
        return directions.NORTH


def _clear():
    print('\n' * 100)


ground_station.init_station()
ground_station.print_ground()

keyboard.hook(check_pressed_key)
keyboard.wait()
