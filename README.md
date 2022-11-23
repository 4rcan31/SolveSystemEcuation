# programa para resolver sistemas de ecuaciones lineales con x incognitas


# main.py
Este archivo contiene el codigo para resolver sistema de dos ecuaciones con dos incognitas, pero ¿y que pasa si quiero agregar una tercera ecuacion con una tercera 
incognita?, pues el programa se rompe, por que solo soporta 2 ecuaciones


# Laplace.py
Del problema anterior surgio este nuevo script, usando el [Teorema de Laplace](https://es.wikipedia.org/wiki/Teorema_de_Laplace) para resolver la determinante
de cualquier matriz y la [Regla de Cramer](https://es.wikipedia.org/wiki/Regla_de_Cramer) para resolver cualquier sistema de ecuaciones

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


 