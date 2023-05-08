import yaml

names_yaml = """
- 'El lenguaje de programacion Python. Challenger-Perez, I., Diaz-Ricardo, Y., & Becerra-Garcia. Programacion. Ciencias Holguin. 2014'
- 'Python para todos. Gonzalez Duque,Programacion. 2011'
- 'mary-kate'
"""

names = yaml.safe_load(names_yaml)

with open('names.yaml', 'w') as file:
    yaml.dump(names, file)

print(open('names.yaml').read())