import pickle

# dump: Serialización y guardado en archivo
data = {"nombre": "Carlos", "edad": 40}
with open('pickle_data.pkl', 'wb') as f:
    pickle.dump(data, f)

# load: Carga desde el archivo
with open('pickle_data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
    print("Pickle Load:", loaded_data)

# dumps: Serializar a bytes
data_bytes = pickle.dumps(data)
print("Pickle Dumps:", data_bytes)

# loads: Deserializar desde bytes
loaded_data_from_bytes = pickle.loads(data_bytes)
print("Pickle Loads:", loaded_data_from_bytes)