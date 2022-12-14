# programa para resolver sistemas de ecuaciones lineales con x incognitas


# systemOfTwoEquations.py
Este archivo contiene el codigo para resolver sistema de dos ecuaciones con dos incognitas, pero ¿y que pasa si quiero agregar una tercera o cuarta ecuacion con una tercera o cuarta incognita?, pues el programa se rompe, por que solo soporta 2 ecuaciones

# systemOfThreeEquations.py
Este archivo contiene el codigo para resolver sistema de tres ecuaciones con tres incognitas, pero ¿y que pasa si quiero agregar una quinta o sexta ecuacion con una quinta o sexta incognita?, pues el programa se rompe, por que solo soporta 3 ecuaciones


# Laplace.py
Del problema anterior surgio este nuevo script, usando el [Teorema de Laplace](https://es.wikipedia.org/wiki/Teorema_de_Laplace) para resolver la determinante de cualquier matriz y la [Regla de Cramer](https://es.wikipedia.org/wiki/Regla_de_Cramer) para resolver cualquier sistema de ecuaciones

# Condiciones
Existen dos condiciones que debemos de cumplir para que el codigo no nos de error 

## 1. numero de ecuaciones = numero de incognitas
 Como lo dice el titulo, el numero de ecuaciones en el sistema tiene que ser igual al numero de incognitas
## 2. la forma ax + bx .. nx = z
  Tambien la forma de la encuacion, el programa al principio nos pregunta cuantas ecuaciones hay en el sistema, digamos que 3

  ax + by + cz = d  
  dx + ey + fz = h  
  ix + jy + kz = l
 
 EL programa solo te pedira las constantes, y hara una matriz como la siguiente
  ```
| x   | y    | z | T.R |
|-----|------|---|-----|
| a   | b    |c  | d   |
| d   | e    |f  | h   |
| i   | j    |k  | l   |
```
Como podemos ver, las `variables` tienen que estar ordenadas, las x en una sola columna, y en otra columna y asi susesivamente

# Instalacion
## 1:
Tienes que instalarte [Python](https://www.python.org/) 
## 2:
clonar el repositorio en la carpeta donde quieras que se descargue haciendo:  
```sh
git clone https://github.com/4rcan31/SolveSystemEcuation.git
```
Si no tienes [Git](https://git-scm.com/) instalado, puedes descargar el codigo en zip desde esta pagina, o simplemente copiar y pegar el codigo
## 3
Una vez ya descargado, puedes ejecutarlo, haciendo  
```sh
python Laplace.py
```
el script cuenta un sistema de debuging para que puedas ver como el script hace las matrices, si quieres verlo puedes ejecutar  
```sh
python Laplace.py debug
```
En el caso que quieras hacer testing con datos aleatorios, el script cuenta con otro script que genera datos aleatorios, para no estar
poniendo todos los datos a mano, para hacerlo puedes ejecutarlo asi

```sh
python Laplace.py random
```

Tambien, en el caso que quieras medir el tiempo de ejecucion en las funciones puedes hacerlo asi
```sh
python Laplace.py time
```

Tambien, puedes ejecutar las tres cosas al mismo tiempo
```sh
python Laplace.py debug random time
```

# Posibles actualizaciones

## 1. tomar datos desde un excel con pandas 


# Posibles optimizaciones

## 1. Algoritmo determinantes
Me he dado cuenta que luego de 10 ecuaciones con 10 incognitas, el tiempo para calcular las determinantes crece demasiado
## 2. Algoritmo de fracciones
Las respuesta ahora se dan en fracciones, pero muy grandes, hay que programar un algoritmo de simplificacion de fracciones eficiente

 