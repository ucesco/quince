import os
import socket
import sys
import atexit

from CMD import Arguments
from Server import StaticHTTPServer

# default port
port = 4000
# default host
host = ''
# default root folder
base = os.path.dirname(os.path.realpath(__file__))

arguments = Arguments(sys.argv)

if arguments.has_arg('b'):
    base = arguments.arg('b')
if arguments.has_arg('p'):
    port = int(arguments.arg('p'))

try:
    server = StaticHTTPServer(socket.AF_INET, socket.SOCK_STREAM, host, port, base)
    server.start()
    print 'Server is running on port ' + str(port)
except Exception as e:
    print 'Failed to start server on port ' + str(port)
    print e
    sys.exit()


def on_exit():
    server.stop()


atexit.register(on_exit)
