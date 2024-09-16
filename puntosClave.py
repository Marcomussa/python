# 1. Variables y Tipos de Datos
x = 5
y = 2.5
z = "Sato"
is_active = True

#! 2. Estructura de Datos
# Arreglos --> Mutables
arr = [1, 2, 3, "Hello", "World"]
print(arr[0])

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

#! 3. Funciones 
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

# 
