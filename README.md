# SolveSystemEcuation

Proyecto en Python para resolver sistemas de ecuaciones lineales.

Este repositorio tiene una idea principal:

> Aprender cómo una computadora puede resolver sistemas de ecuaciones usando matrices, determinantes y la Regla de Cramer.

No necesitas ser experto en programación para entender el proyecto.
Tampoco necesitas saber mucha matemática avanzada. La intención es mostrar el proceso paso a paso, desde una ecuación escrita de forma normal hasta un programa que puede resolver sistemas más grandes.

---

## 1. ¿Qué problema resuelve este proyecto?

Un sistema de ecuaciones lineales es un grupo de ecuaciones que comparten variables.

Por ejemplo:

```text
2x + 3y = 8
4x - y = 2
```

Aquí hay dos incógnitas:

```text
x
y
```

Resolver el sistema significa encontrar qué valores deben tener `x` y `y` para que ambas ecuaciones sean verdaderas al mismo tiempo.

El proyecto empieza resolviendo sistemas pequeños y luego evoluciona hasta resolver sistemas de cualquier tamaño cuadrado, como:

```text
2 x 2
3 x 3
4 x 4
5 x 5
...
```

Un sistema cuadrado significa que tiene el mismo número de ecuaciones que de incógnitas.

---

## 2. La idea general del proyecto

El proyecto sigue este camino:

```text
Ecuaciones normales
        ↓
Números separados
        ↓
Matriz de coeficientes
        ↓
Determinantes
        ↓
Regla de Cramer
        ↓
Resultado final
```

La idea no es solamente obtener la respuesta, sino entender cómo se llega a ella.

---

## 3. Cómo se convierte una ecuación en datos para el programa

El programa no recibe la ecuación escrita así:

```text
2x + 3y = 8
```

En lugar de eso, recibe solo los números:

```text
2
3
8
```

Eso significa:

```text
2x + 3y = 8
```

Los primeros números son los coeficientes de las variables.
El último número es el resultado de la ecuación.

Por ejemplo:

```text
4x - y = 2
```

Se ingresa como:

```text
4
-1
2
```

Porque realmente significa:

```text
4x + (-1)y = 2
```

---

## 4. Ejemplo completo de entrada

Supongamos este sistema:

```text
2x + 3y = 8
4x - y = 2
```

El programa necesita leerlo como filas de números:

```text
[2, 3, 8]
[4, -1, 2]
```

Cada fila representa una ecuación.

La estructura es:

```text
[coeficiente de x, coeficiente de y, resultado]
```

Para un sistema de tres variables:

```text
2x + y - z = 8
-3x - y + 2z = -11
-2x + y + 2z = -3
```

Se ingresa así:

```text
[2, 1, -1, 8]
[-3, -1, 2, -11]
[-2, 1, 2, -3]
```

La estructura es:

```text
[coeficiente de x, coeficiente de y, coeficiente de z, resultado]
```

---

## 5. Qué es una matriz en este proyecto

Una matriz es una forma ordenada de guardar números en filas y columnas.

Por ejemplo, este sistema:

```text
2x + 3y = 8
4x - y = 2
```

Tiene esta matriz de coeficientes:

```text
| 2   3 |
| 4  -1 |
```

Y esta columna de resultados:

```text
| 8 |
| 2 |
```

El programa separa el sistema en esas dos partes:

```text
coeficientes  → números que acompañan a las variables
resultados    → números después del signo igual
```

---

## 6. Qué método matemático usa

El proyecto usa la Regla de Cramer.

La Regla de Cramer permite resolver algunos sistemas de ecuaciones usando determinantes.

La idea básica es:

1. Se construye la matriz principal del sistema.
2. Se calcula su determinante principal, llamado `D`.
3. Para cada variable, se construye una nueva matriz.
4. En esa nueva matriz se reemplaza una columna por la columna de resultados.
5. Se calcula el determinante de esa nueva matriz.
6. La solución de cada variable se obtiene dividiendo.

Para un sistema de dos variables:

```text
x = Dx / D
y = Dy / D
```

Para un sistema de tres variables:

```text
x = Dx / D
y = Dy / D
z = Dz / D
```

El sistema tiene solución única cuando:

```text
D != 0
```

Si `D = 0`, significa que el sistema no tiene una solución única usando este método.

---

## 7. Evolución del repositorio

El repositorio está dividido en tres programas principales.

```text
systemOfTwoEquations.py
systemOfThreeEquations.py
Laplace.py
```

Cada archivo representa una etapa diferente de aprendizaje.

---

## 8. Primera etapa: `systemOfTwoEquations.py`

Este archivo resuelve sistemas de 2 ecuaciones con 2 incógnitas.

Ejemplo:

```text
2x + 3y = 8
4x - y = 2
```

Este es el caso más pequeño donde ya se puede ver claramente cómo funciona la Regla de Cramer.

### Qué enseña este archivo

Este archivo enseña la base del proyecto:

```text
leer datos
crear matrices
calcular determinantes
dividir determinantes
mostrar resultados
```

Aquí todo está pensado para dos variables:

```text
x
y
```

Por eso es fácil de seguir.

### Limitación

Solo sirve para sistemas `2 x 2`.

Si se intenta resolver un sistema de tres variables, este archivo ya no alcanza.

---

## 9. Segunda etapa: `systemOfThreeEquations.py`

Este archivo resuelve sistemas de 3 ecuaciones con 3 incógnitas.

Ejemplo:

```text
2x + y - z = 8
-3x - y + 2z = -11
-2x + y + 2z = -3
```

Ahora hay tres variables:

```text
x
y
z
```

Por eso se calculan más determinantes:

```text
D
Dx
Dy
Dz
```

### Qué enseña este archivo

Este archivo muestra que la misma idea de Cramer puede extenderse a sistemas más grandes.

Pero también muestra un problema importante:

> Mientras más grande es el sistema, más difícil se vuelve escribir todas las fórmulas a mano.

Pasar de `2 x 2` a `3 x 3` ya requiere más código.
Pasar a `4 x 4` sería todavía más largo.
Pasar a `5 x 5` sería peor.

Por eso aparece el tercer archivo.

---

## 10. Tercera etapa: `Laplace.py`

Este es el archivo principal del proyecto.

Su objetivo es resolver sistemas cuadrados de cualquier tamaño:

```text
2 x 2
3 x 3
4 x 4
5 x 5
...
```

La diferencia es que este archivo ya no depende de fórmulas escritas manualmente para cada tamaño.

En lugar de eso, usa un proceso general.

---

## 11. Qué hace `Laplace.py`

El proceso de `Laplace.py` es este:

```text
1. Pregunta cuántas variables tiene el sistema.
2. Pide los coeficientes y resultados de cada ecuación.
3. Separa los coeficientes de los resultados.
4. Construye la matriz principal.
5. Construye las matrices necesarias para Cramer.
6. Calcula los determinantes.
7. Calcula el valor de cada variable.
8. Muestra el resultado.
```

En otras palabras:

```text
Laplace.py automatiza lo que los primeros archivos hacían manualmente.
```

---

## 12. Qué es el Teorema de Laplace en este proyecto

El Teorema de Laplace se usa para calcular determinantes de matrices grandes.

La idea simple es esta:

> Una matriz grande puede romperse en matrices más pequeñas.

Entonces el programa calcula el determinante de una matriz grande reduciendo el problema poco a poco.

Por ejemplo:

```text
determinante de una matriz 4 x 4
        ↓
varios determinantes 3 x 3
        ↓
varios determinantes 2 x 2
        ↓
resultado final
```

Esto se llama recursividad.

---

## 13. Qué es recursividad

Recursividad significa que una función se llama a sí misma para resolver un problema más pequeño.

En este proyecto, la recursividad aparece cuando se calcula un determinante.

La lógica es:

```text
Si la matriz es 2 x 2:
    usar la fórmula directa

Si la matriz es más grande:
    dividirla en matrices más pequeñas
    calcular sus determinantes
    combinar los resultados
```

Por eso `Laplace.py` puede trabajar con matrices de diferentes tamaños.

---

## 14. Archivos del proyecto

### `systemOfTwoEquations.py`

Primera versión.

Resuelve únicamente sistemas `2 x 2`.

Es útil para entender la Regla de Cramer de la forma más simple posible.

---

### `systemOfThreeEquations.py`

Segunda versión.

Resuelve únicamente sistemas `3 x 3`.

Es útil para ver cómo la misma idea crece, pero también para notar que escribir todo a mano no escala bien.

---

### `Laplace.py`

Versión general.

Resuelve sistemas cuadrados de cualquier tamaño usando:

```text
matrices
determinantes
Regla de Cramer
Teorema de Laplace
recursividad
```

Este es el archivo más importante del proyecto.

---

## 15. Requisitos

Para ejecutar el proyecto necesitas tener instalado:

* Python
* Opcionalmente Git

No se necesitan librerías externas importantes para usar el proyecto.

---

## 16. Cómo descargar el proyecto

Con Git:

```sh
git clone https://github.com/4rcan31/SolveSystemEcuation.git
```

Luego entra a la carpeta:

```sh
cd SolveSystemEcuation
```

También puedes descargar el repositorio como archivo `.zip` desde GitHub.

---

## 17. Cómo ejecutar los programas

Para ejecutar la versión de dos ecuaciones:

```sh
python systemOfTwoEquations.py
```

Para ejecutar la versión de tres ecuaciones:

```sh
python systemOfThreeEquations.py
```

Para ejecutar la versión general:

```sh
python Laplace.py
```

En algunos sistemas puede ser necesario usar:

```sh
python3 Laplace.py
```

---

## 18. Cómo usar `Laplace.py`

Ejecuta:

```sh
python Laplace.py
```

El programa preguntará:

```text
Ingrese cuantas variables tiene su sistema de ecuaciones:
```

Si escribes:

```text
3
```

Entonces el programa entenderá que resolverás un sistema de tres variables.

Después deberás ingresar los coeficientes y el resultado de cada ecuación.

Ejemplo:

```text
2x + y - z = 8
-3x - y + 2z = -11
-2x + y + 2z = -3
```

Se ingresa así:

```text
3

2
1
-1
8

-3
-1
2
-11

-2
1
2
-3
```

La primera línea indica la cantidad de variables.

Luego cada grupo representa una ecuación.

---

## 19. Modos especiales de `Laplace.py`

`Laplace.py` acepta algunas palabras especiales al ejecutarse.

### Modo debug

```sh
python Laplace.py debug
```

Muestra información interna del programa.

Sirve para ver cosas como:

```text
datos originales
matrices generadas
determinantes calculados
resultado final
```

Este modo es útil para estudiar cómo trabaja el algoritmo.

---

### Modo random

```sh
python Laplace.py random
```

Genera datos aleatorios en lugar de pedirlos manualmente.

Sirve para probar el programa rápidamente.

---

### Modo time

```sh
python Laplace.py time
```

Muestra tiempos de ejecución.

Sirve para observar cuánto tarda el programa, especialmente con sistemas grandes.

---

### Combinar modos

También se pueden combinar:

```sh
python Laplace.py debug random time
```

El orden no es importante.

---

## 20. Cómo leer el proyecto en orden

La mejor forma de entender este repositorio es seguir este camino:

```text
1. Probar systemOfTwoEquations.py
2. Entender cómo se resuelve un sistema 2 x 2
3. Probar systemOfThreeEquations.py
4. Ver cómo crece el problema en 3 x 3
5. Probar Laplace.py
6. Entender cómo se generaliza el proceso
```

La idea es ver la evolución:

```text
caso pequeño
    ↓
caso más grande
    ↓
problema de escalabilidad
    ↓
algoritmo general
```

---

## 21. Conceptos importantes

### Coeficiente

Es el número que acompaña a una variable.

En:

```text
5x
```

El coeficiente es:

```text
5
```

---

### Incógnita

Es el valor que queremos encontrar.

Por ejemplo:

```text
x
y
z
```

---

### Término independiente

Es el número que está después del signo igual.

En:

```text
2x + 3y = 8
```

El término independiente es:

```text
8
```

---

### Matriz

Es una tabla de números organizada en filas y columnas.

---

### Determinante

Es un valor que se calcula a partir de una matriz cuadrada.

En este proyecto se usa para saber si el sistema puede resolverse con Cramer y para calcular las soluciones.

---

### Sistema cuadrado

Es un sistema donde el número de ecuaciones es igual al número de incógnitas.

Ejemplos:

```text
2 ecuaciones y 2 incógnitas
3 ecuaciones y 3 incógnitas
4 ecuaciones y 4 incógnitas
```

---

## 22. Limitaciones actuales

### El método puede volverse lento

El cálculo de determinantes por Laplace es fácil de entender, pero no es el método más eficiente para matrices grandes.

Para sistemas pequeños funciona bien.

Para sistemas grandes, el tiempo de ejecución puede crecer mucho.

---

### Solo trabaja directamente con sistemas cuadrados

El proyecto está pensado para sistemas donde hay el mismo número de ecuaciones e incógnitas.

No está diseñado para resolver directamente sistemas como:

```text
2 ecuaciones y 3 incógnitas
4 ecuaciones y 2 incógnitas
```

---

### Los primeros archivos son didácticos

`systemOfTwoEquations.py` y `systemOfThreeEquations.py` no buscan ser la solución final.

Existen para mostrar el camino de aprendizaje.

La versión más general es:

```text
Laplace.py
```

---

## 23. Qué se aprende con este proyecto

Este proyecto ayuda a entender varias ideas importantes:

```text
cómo representar ecuaciones con números
cómo convertir ecuaciones en matrices
cómo usar determinantes
cómo aplicar la Regla de Cramer
cómo generalizar un algoritmo
cómo usar recursividad
por qué una solución manual no siempre escala
```

La parte más importante no es solamente que el programa resuelva sistemas.

Lo más importante es ver cómo una idea matemática se convierte poco a poco en un algoritmo.

---

## 24. Resumen final

`SolveSystemEcuation` es un proyecto didáctico sobre sistemas de ecuaciones lineales.

Empieza con soluciones pequeñas y manuales:

```text
2 x 2
3 x 3
```

Y termina con una solución general:

```text
n x n
```

El proyecto muestra el proceso completo:

```text
ecuación
    ↓
coeficientes
    ↓
matriz
    ↓
determinantes
    ↓
Regla de Cramer
    ↓
resultado
```

Por eso este repositorio puede leerse como un camino de aprendizaje:

> primero entender el caso simple, luego ver por qué no escala, y finalmente construir una solución general.
