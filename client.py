import socket
import json

HOST, PORT = "localhost", 9527
data = {
"name": "Hola, Soy Tom.",
"age": 10,
"info": "Muestra de información."
}

# Crear un socket(SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectar con el servidor y enviar datos
    sock.connect((HOST, PORT))
    sock.send(bytes(json.dumps(data), 'UTF-8'))

    # Recibe datos del servidor y se apaga
    received = json.loads(sock.recv(1024).decode('UTF-8'))
finally:
    sock.close()

print ("Enviado: {}".format(data))
print ("Recivido: {}".format(received))