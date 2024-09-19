## Excepciones
Es una muy mala practica atrapar cualquier excepcion. Estas deben atrapar cierto escenario en especifico. 

## Manejo de Archivos
El parametro Mode de Open posee 4 parametros posibles: 
    - r , solo lectura
    - w , escritura (sobreescribe)
    - a , appendea al final
    - x , crea archivo nuevo, si ya existe => lanza error
    - b , modo binario

Logramos Persistencia (acción de conservar la información un objeto de forma permanente, pero también de recuperarla) Serializando los objetos. Hecha la Serializacion, se debe Deserializar.

Que significa "Serializar" un objeto?
- Es el proceso de convertir un objeto o estructura de datos (como una lista, diccionario, o clase) en un formato que pueda ser almacenado o enviado fácilmente, como una cadena de texto o datos binarios. Luego, ese formato puede ser reconvertido (deserializado) para recuperar el objeto original.

Modulos para serializar y guardar objetos: 
    - Pickle .pkl
    - Dill .dill
    - JSON .json
    - Shelve

**Pickle** Conviene usarse cuando necesitas guardar cualquier objeto de Python (listas, diccionarios, clases, etc.) y recuperar exactamente ese objeto más tarde. No se usa para intercambiar datos entre diferentes nodos. 

**Dill** Extiende las capacidades de pickle, permitiendo serializar objetos más complejos como funciones, lambdas o clases con estados avanzados.

**JSON** Es ideal para intercambiar informacion entre nodos. No soporta objetos complejos como funciones o clases.

**Shelve** Se usa cuando necesitas almacenamiento persistente basado en clave-valor (diccionarios). No es adecuado para compartir datos entre sistemas.