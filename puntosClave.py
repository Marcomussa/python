# 1. Variables y Tipos de Datos
x = 5
y = 2.5
z = "Sato"
is_active = True

#! 2. Estructura de Datos
# Arreglos --> Mutables
list = [1, 2, 3, "Hello", "World"]
print(list[0])

# Tuplas --> Inmutables
tupla = (10, 20, 30)
print(tupla[0])

# Sets --> Unicos e Inmutables
set = {1, 2, 2, 2, 3}
print(set) # output: {1, 2, 3}

# Diccionarios
dict = {
    "name": "Marco",
    "surname": "Mussa"
}
print(dict["name"])

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

# Anidacion
def externa(text):
    def interna():
        return text.upper()
    return interna()

print(externa("sato"))
