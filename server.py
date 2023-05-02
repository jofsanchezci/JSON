import socketserver, subprocess, sys
from threading import Thread
from pprint import pprint
import json

HOST = 'localhost'
PORT = 9527

class SingleTCPHandler(socketserver.BaseRequestHandler):
    "Una instancia por conexión"
    def handle(self):
        # self.request es la conexión del cliente
        data = self.request.recv(1024)  # entrada de clip a 1Kb
        text = data.decode('utf-8')
        pprint(json.loads(text))
        for key in json.loads(text):
            pprint(json.loads(text)[key])
        self.request.send(bytes(json.dumps({"status":"Exitosa!"}), 'UTF-8'))
        self.request.close()

class SimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # Ctrl-C matará limpiamente todos los hilos generados
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)

if __name__ == "__main__":
    server = SimpleServer((HOST, PORT), SingleTCPHandler)
    # terminar con Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)