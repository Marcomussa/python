import json

archivo_json = 'data.json'

with open(archivo_json, 'r') as archivo:
    datos = json.load(archivo)

# Recorrer cada elemento de la lista
for elemento in datos:
    print(f"ID: {elemento['id']}")
    print(f"Nombre: {elemento['first_name']}")
    print(f"IP Address: {elemento['ip_address']}")
    print("-" * 30)  # Separador entre registros
