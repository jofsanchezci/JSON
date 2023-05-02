import json
with open('data.json') as file:
    data = json.load(file)

    for client in data['clientes']:
        print('Primer nombre:', client['first_name'])
        print('Apellido:', client['last_name'])
        print('Edad:', client['age'])
        print('Altura:', client['altura'])
        print('++++++++++++++++++')