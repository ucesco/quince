class HTTPResponse:
    def __init__(self, connection):
        self.__connection = connection

    def send(self, content):
        self.__connection.send(content)

    def send_404(self):
        self.__connection.send('HTTP/1.0 404 Not Found')
