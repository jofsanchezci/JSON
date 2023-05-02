import json

data = {}
data['clientes'] = []

data['clientes'].append({
    'first_name': 'Juan',
    'last_name': 'Perez',
    'age': 27,
    'altura': 7.17})

data['clientes'].append({
    'first_name': 'Pedro',
    'last_name': 'Rodriguez',
    'age': 31,
    'altura': [1.90, 5.50]})

data['clientes'].append({
    'first_name': 'Teo',
    'last_name': 'Rivera',
    'age': 36,
    'altura': 1.11})

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)