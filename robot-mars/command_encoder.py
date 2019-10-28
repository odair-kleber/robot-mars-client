import directions

__DIR_RIGHT = 'R'
__DIR_LEFT = 'L'
__DIR_NONE = ''
__MOV = 'M'


def encode_command_movement() -> str:
    return __MOV


def encode_command_direction(last_direction: str, new_direction: str) -> str:
    if last_direction == directions.NORTH:
        return __encode_direction_from_north(new_direction)
    elif last_direction == directions.EAST:
        return __encode_direction_from_east(new_direction)
    elif last_direction == directions.SOUTH:
        return __encode_direction_from_south(new_direction)
    elif last_direction == directions.WEST:
        return __encode_direction_from_west(new_direction)
    else:
        return __DIR_NONE


def __encode_direction_from_north(direction: str) -> str:
    if direction == directions.EAST:
        return __DIR_RIGHT
    elif direction == directions.SOUTH:
        return __DIR_RIGHT * 2
    elif direction == directions.WEST:
        return __DIR_LEFT
    else:
        return __DIR_NONE


def __encode_direction_from_east(direction: str) -> str:
    if direction == directions.SOUTH:
        return __DIR_RIGHT
    elif direction == directions.WEST:
        return __DIR_RIGHT * 2
    elif direction == directions.NORTH:
        return __DIR_LEFT
    else:
        return __DIR_NONE


def __encode_direction_from_south(direction: str) -> str:
    if direction == directions.WEST:
        return __DIR_RIGHT
    elif direction == directions.NORTH:
        return __DIR_RIGHT * 2
    elif direction == directions.EAST:
        return __DIR_LEFT
    else:
        return __DIR_NONE


def __encode_direction_from_west(direction: str) -> str:
    if direction == directions.NORTH:
        return __DIR_RIGHT
    elif direction == directions.EAST:
        return __DIR_RIGHT * 2
    elif direction == directions.SOUTH:
        return __DIR_LEFT
    else:
        return __DIR_NONE
