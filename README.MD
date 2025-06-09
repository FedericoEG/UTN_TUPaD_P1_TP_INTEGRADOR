# Trabajo Práctico Integrador
### Materia: Programación I
### Alumnos: Federico Esteban Garcia y Federico Garcia Bengolea
### Comisión: 14

## Docentes
### Profesor/a: Ariel Enferrel
### Tutor/a: Ramiro Hualpa

## Descripción
Este repositorio contiene los archivos del caso práctico detallado en el cuerpo del trabajo práctico
#### Detalle
La aplicación solicita inicialmente dos valores. El primero va a ser utilizado para confeccionar una lista de valores random. Se solicita un valor entre 1.000 y 5.000 los cuales van a ser los elementos que posteriormente se recorren con un loop para ir agregando los elementos como nodos de dos árboles.
El segundo valor es un número entre 3 y 9 el cual debe ser un número impar. Este será utilizado como el grado del arbol tipo B.
La aplicación automáticamente genera un árbol del tipo BST y uno tipo B con los mismos valores. Luego, y también de manera automática se toma un valor aleatorio que se encuentra en ambos árboles y un valor que no se encuentra en los árboles. Y se realiza una búsqueda en cada uno de ellos.
Luego se genera un informe de este tipo:
```
======================= Análisis de Datos =======================

Datos:
Cantidad de elementos en los árboles:              1000000
Grado del árbol tipo B:                            3
Elemento existente buscado en ámbos árboles:       157734
Elemento NO existente buscado en ámbos árboles:    2977593
Elemento medio existente buscado en ámbos árboles: 500000

Tiempos:
Tiempo en árbol BST para elemento existente:       0.000010014
Tiempo en árbol B para elemento existente:         0.000014782
Tiempo en árbol BST para elemento NO existente:    0.000003099
Tiempo en árbol B para elemento NO existente:      0.000009298
Tiempo en árbol BST para elemento medio:           0.000006199
Tiempo en árbol B para elemento medio:             0.000008821

=================================================================

Promedio de búsquedas en árbol BST:  0.000006437
Promedio de búsquedas en árbol B:    0.000010967

=================================================================
```

## Utilización
Para poder utilizar el programa es necesario tener instalada la dependencia `COLORAMA`. Ésta puede ser instalada mediante el compando `pip install colorama` o bien utilizando el archivo `requirements.txt` que se encuentra en el repositorio. Para realizar la instalación mediante el archivo de requerimientos se puede utilizar el comando `pip install -r requirements.txt`.

Una vez instalada la dependecia necesaria se puede proceder a ejecutar el programa corriendo el comendo `python main.py`.