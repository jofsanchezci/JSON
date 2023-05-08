import json

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

with open('libro.json', 'w') as file:
    json.dump(data, file, indent=4)