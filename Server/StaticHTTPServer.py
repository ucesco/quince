from HTTP import HTTPRequest, HTTPResponse
from Server import HTTPServer


class StaticHTTPServer(HTTPServer):
    def __init__(self, socket_family, socket_type, host, port, base):
        HTTPServer.__init__(self, socket_family, socket_type, host, port, base)

    def start(self):
        HTTPServer.start(self)

        # TODO: Implement with threads to handle multiple request
        while True:
            connection, address = self._socket.accept()
            # TODO: Need to handle request bigger than 1024
            request_str = connection.recv(1024)
            request = HTTPRequest(request_str)
            response = HTTPResponse(connection)

            try:
                with open(self._base + request.path, 'r') as content_file:
                    response.send(content_file.read())
            except IOError:
                response.send_404()
            finally:
                connection.close()



