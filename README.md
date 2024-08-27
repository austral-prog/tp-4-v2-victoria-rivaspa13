[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/aXVp-yNa)
# prog1-tp4-template

## Ejercicio 1 - Line

Queremos hacer un programa que nos calcule para una ecuación de primer grado la distancia sobre la recta entre dos
coordenadas cualquiera del eje X y además me informe de las coordenadas del eje Y a la que corresponde.

Ejemplo:
```
Ingrese el coeficiente A: 2.3
Ingrese el coeficiente B: -4
Ingrese el coeficiente X1: 50
Ingrese el coeficiente X2: -32.9
El coeficiente A de su ecuación de la recta es: 2.3
El coeficiente B de su ecuación de la recta es: -4.0
El coeficiente X1 de su ecuación de la recta es: 50.0
El coeficiente X2 de su ecuación de la recta es: -32.9

Para la siguiente ecuación:
	Y = 2.3X + -4.0

Dados los siguientes puntos:
	P1 (50.0, 110.99999999999999)
	P2 (-32.9, -79.66999999999999)

La distancia entre ellos es: 207.9121422620622
```
************************************************** 


HINT: [Formula de la distancia](https://es.wikipedia.org/wiki/Distancia#Distancia_de_dos_puntos_en_el_plano)

HINT: [Python Math doc](https://www.w3schools.com/python/module_math.asp)


## Ejercicio 2 - Leap Year

Un año no tiene en realidad 365 días, sino 365.242199. A fin de mantener el calendario en fase con los equinoccios y los solsticios, Julio César adoptó un sistema que añade un día adicional a cada cuatro años, que se conoce como año bisiesto. No obstante, este sistema no tenía la suficiente precisión, por lo que el Papa Gregorio XIII decretó, en 1582, un nuevo sistema calendario, según el cual un año divisible entre cuatro es bisiesto a menos que sea un año centenario, en cuyo caso sólo es bisiesto si es divisible por 400. Escribir una función que informa si un año dado es bisiesto.

Hacer un programa que dado un año me indique si es bisiesto útilizando al menos un comparador `or` o `and`.

Ejemplos:
```
Ingrese un año: 2000
El año 2000 es bisiesto
```
```
Ingrese un año: 2001
El año 2001 no es bisiesto
```