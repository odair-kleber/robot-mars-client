import command_encoder
import cursors
import directions
import message_decoder
import satellite
from robot import RobotPosition

__BOUNDS = 5
__DEFAULT_CHAR_GROUND = ' \u25a2 '

__plain = []
__chain_command = ''

last_pos_x = 0
last_pos_y = 0
last_dir = 'N'


def init_station():
    __init_plain()
    __set_robot_position(0, 0, directions.NORTH)


def print_ground():
    for x in __plain:
        for y in x:
            print(y, end='')
        print()


def mov_robot():
    pass
    # todo: to implement api


def set_robot_direction(direction):
    global __chain_command
    __chain_command += command_encoder.encode_command_direction(last_dir, direction)
    new_robot_pos = __send_message_to_mars(__chain_command)
    __set_robot_position(new_robot_pos.x, new_robot_pos.y, new_robot_pos.direction)
    # todo: to implement api request


def __init_plain():
    for _ in range(0, __BOUNDS):
        temp = []
        for _ in range(0, __BOUNDS):
            temp.append(__DEFAULT_CHAR_GROUND)
        __plain.append(temp)


def __send_message_to_mars(message: str) -> RobotPosition:
    conn = satellite.start_connection()
    mars_response = conn.send_message_to_mars(message)
    return message_decoder.decode_robot_position(mars_response)


def __set_robot_position(x, y, direction):
    __clear_robot_position()

    if direction == directions.NORTH:
        __plain[x][y] = cursors.UP
    elif direction == directions.SOUTH:
        __plain[x][y] = cursors.DOWN
    elif direction == directions.EAST:
        __plain[x][y] = cursors.RIGHT
    elif direction == directions.WEST:
        __plain[x][y] = cursors.LEFT

    global last_pos_x, last_pos_y, last_dir
    last_pos_x = x
    last_pos_y = y
    last_dir = direction


def __clear_robot_position():
    __plain[last_pos_x][last_pos_y] = __DEFAULT_CHAR_GROUND
