import socket

from abc import ABCMeta


class HTTPServer:
    __metaclass__ = ABCMeta

    def __init__(self, socket_family, socket_type, host, port, base=None):
        self._socket_family = socket_family
        self._socket_type = socket_type
        self._host = host
        self._port = port
        self._base = base

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self._socket.bind((self._host, self._port))
        self._socket.listen(5)

    def stop(self):
        return

