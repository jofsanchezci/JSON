import socket
import json

HOST, PORT = "localhost", 9527
data = {}
data['Libros'] = []

data['Libros'].append({
    'Titulo': 'El lenguaje de programación Python',
    'Autores': 'Challenger-Pérez, I., Díaz-Ricardo, Y., & Becerra-García',
    'Tema': 'Programación',
    'Editorial': 'Ciencias Holguín',
    'Año': 2014})

data['Libros'].append({
    'Titulo': 'Python para todos',
    'Autores': 'González Duque',
    'Tema': 'Programación',
    'Editorial': 'NA',
    'Año':2011})

data['Libros'].append({
    'Titulo': 'Los elementos del periodismo',
    'Autores': 'Kovach, B., & Rosenstiel, T',
    'Tema': 'Periodimos',
    'Editorial':'Aguilar',
    'Año': 2012})

data['Libros'].append({
    'Titulo': 'Los dueños del periodismo ',
    'Autores': 'Reig, R. ',
    'Tema': 'Periodismo',
    'Editorial': 'Editorial Gedisa',
    'Año':2011})

data['Libros'].append({
    'Titulo': 'Actividades físicas y deportes adaptados para personas con discapacidad',
    'Autores': 'Rivas, D. S',
    'Tema': 'Deportes',
    'Editorial': 'Paidotribo',
    'Año':2013}) 


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