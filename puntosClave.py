import pickle
import json
import os

# 1. Variables y Tipos de Datos --> Inmutables. 
x = 5
y = 2.5
z = "Sato"
is_active = True

#! 2. Estructura de Datos
# Tuplas --> Inmutables
tupla = (10, 20, 30)
print(tupla[0])

# Sets --> Unicos e Inmutables
set = {1, 2, 2, 2, 3}
print(set) # output: {1, 2, 3}

# Arreglos --> Mutables
list = [1, 2, 3, "Hello", "World"]
print(list[0])

# Diccionarios --> Mutables
dict = {
    "name": "Marco",
    "surname": "Mussa"
}
print(dict["name"])

#* Recorrerlas
for elemento in list:
    print(elemento)

#! 3. Metodos
string = "Hello World"
string.uppper()
string.lower()
string.capitalize()
string.strip() # Elimina espacios en blanco
string.replace("Hello", "Goodbye")
string.split(" ") # ["Hello", "World"]

list.append(4)
list.extend([4, 5])
list.insert(2, 3) # En indice 2, inserta value 3
list.remove(3) # Elimina la primera aparicion del parametro
list.pop() # Elimina el ultimo. Si se le pasa parametro elimina el de dicho indice
list.sort() # Ordena ascendente
list.reverse() # Invierte orden
list.index(2) # Devuelve el indice de la primera aparicion del elemento
list.clear() # []
list.push(0)
list.append(0)

dict.get("name")
dict.keys()

#! 4. Funciones 
#* Son objetos de primera clase --> Se pueden pasar como parametros a otras funciones o asignarlas a variables 
# Parametros
def func(name):
    return f"Hello {name}" # f-strings

result = func("Sato")
print(result)

# Valores x Defecto
def func_defect_value(name="Sato"):
    return f"Hello {name}"

func_defect_value() # Hello Sato
func_defect_value("Marco") # Hello Marco

# Retorno de Valores
def sum(a,b):
    return a + b

# Funciones como objetos de primera clase
def square(x):
    return x ** 2

def apply_func(function, value):
    return function(value)

result = apply_func(square, 2)

# Anidacion o Clausuras
def externa(text):
    def interna():
        return text.upper()
    return interna()

print(externa("sato"))

# Cantidad variable de parametros
def suma_cuadrados(*args):
    return

suma_cuadrados((1))
suma_cuadrados((1, 2))
suma_cuadrados((1, 2, 3))

# Parametros de tipo Key-Value
def show_details(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

show_details(name="Sato", lang="Python")

#! 5. Condicionales
numero = 5
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
    
#! Palabras Reservadas
# nonlocal --> Indicamos que la variable no pertenece a su scope perteneciente. Permite que una funcion interna modifique el valor de una variable ubicada por fuera de esta. 

#! POO
class Persona:
    def __init__(self, nombre, edad): # init --> Constructor
        self.nombre = nombre
        self.edad = edad
    
    def printPersona(self): # En los metodos, siempre que se referencie a una propiedad "self" debe estar
        print(f"{self.nombre}, {self.edad}")
        
persona = Persona("Sato", 23)
persona.nombre
persona.printPersona()

#* Herencia
class Empleado(Persona): 
    def __init__(self, nombre, edad, ocupacion):
        super().__init__(nombre, edad) # Propiedades heredadas
        
        
#! Manejo de Excepciones --> Manejar errores en tiempo de ejecucion
try:
    num = int(input("Ingresa un número: "))
    resultado = 10 / num
except ValueError:
    # Captura si no se puede convertir la entrada a entero
    print("Error: Entrada no válida.")
except ZeroDivisionError:
    # Captura la excepción de división por cero
    print("Error: No se puede dividir por cero.")
except Exception as e:
    # Captura cualquier otra excepción
    print(f"Ocurrió un error inesperado: {e}")
else:
    print('No hay excepciones en el bloque principal')
finally:
    print('Esto se ejecuta siempre')


#! Manejo de Archivos
# Estructura general
open('', mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

archivo = open("archivo.txt", mode="w", encoding="utf-8")

# Lectura
archivo.read()
archivo.readline()
archivo.readlines()
archivo.close() # --> Siempre cerrarlo

# Escritura
archivo.write("Hello World")
archivo.close() 

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

#? Pickle
data = {"name": "Alice", "age": 25}
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f) # Serializa y lo escribe en f

# Deserialización con pickle
with open('data.pickle', 'rb') as f:
    loaded_data = pickle.load(f)
    print(loaded_data)  # {'name': 'Alice', 'age': 25}
