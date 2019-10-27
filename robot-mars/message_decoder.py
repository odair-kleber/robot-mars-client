import re

from robot import RobotPosition

__DEFAULT_ENCODING = 'utf-8'
__pattern = r"^\"\((\d{1}),(\d{1}),(N|S|W|E)\)\"$"


def decode_robot_position(message: bytes) -> RobotPosition:
    msg_decoded = message.decode(__DEFAULT_ENCODING)
    match = re.match(__pattern, msg_decoded)
    if match is None:
        return None

    groups = match.groups()
    if groups.__len__() != 3:
        return None

    return RobotPosition(int(groups[0]), int(groups[1]), groups[2])
