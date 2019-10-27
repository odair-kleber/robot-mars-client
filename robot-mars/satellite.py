import requests

import mars_station


class SatteliteConnection(object):
    __STATUS_CODE_OK = 200

    def __init__(self):
        pass

    def send_message_to_mars(self, message):
        response = requests.post(mars_station.ADDRESS + '/' + message)
        if response.status_code == self.__STATUS_CODE_OK:
            return response.content


def start_connection() -> SatteliteConnection:
    return SatteliteConnection()
