import command_encoder
import cursors
import directions
import message_decoder
import satellite
from robot import RobotPosition

__BOUNDS = 6
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
    mov_command = command_encoder.encode_command_movement()
    full_command = __inc_command(mov_command)
    new_robot_pos = __send_message_to_mars(full_command)
    if new_robot_pos is not None:
        __set_robot_position(new_robot_pos.x, new_robot_pos.y, new_robot_pos.direction)
    else:
        __dec_command(mov_command)


def set_robot_direction(direction):
    dir_command = command_encoder.encode_command_direction(last_dir, direction)
    full_command = __inc_command(dir_command)
    new_robot_pos = __send_message_to_mars(full_command)
    if new_robot_pos is not None:
        __set_robot_position(new_robot_pos.x, new_robot_pos.y, new_robot_pos.direction)
    else:
        __dec_command(dir_command)


def __init_plain():
    for _ in range(0, __BOUNDS):
        temp = []
        for _ in range(0, __BOUNDS):
            temp.append(__DEFAULT_CHAR_GROUND)
        __plain.append(temp)


def __send_message_to_mars(message: str) -> RobotPosition:
    conn = satellite.start_connection()
    mars_response = conn.send_message_to_mars(message)
    if mars_response is not None:
        return message_decoder.decode_robot_position(mars_response)


def __set_robot_position(x, y, direction):
    __clear_robot_position()
    x = __invert_x(x)

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


def __invert_x(x):
    x -= 5
    if x < 0:
        x *= -1
    return x


def __inc_command(new_command: str) -> str:
    global __chain_command
    __chain_command += new_command
    return __chain_command


def __dec_command(new_command: str) -> str:
    global __chain_command
    __chain_command = __chain_command[:-new_command.__len__()]
    return __chain_command
