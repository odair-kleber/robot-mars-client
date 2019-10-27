class RobotPosition(object):
    def __init__(self, x: int, y: int, direction: str):
        self._x = x
        self._y = y
        self._direction = direction

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def direction(self) -> str:
        return self._direction
