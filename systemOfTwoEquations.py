def result(determinats):
    x = determinats[1] / determinats[0]
    y = determinats[2] / determinats[0]
    return [x, y]
  
  
def determinant(matrix):
    d  = matrix[0][0] * matrix[0][3] - matrix[0][1] * matrix[0][2]
    dx = matrix[1][0] * matrix[1][3] - matrix[1][1] * matrix[1][2] 
    dy = matrix[2][0] * matrix[2][3] - matrix[2][1] * matrix[2][2]
    return [d, dx, dy]
  
  
def matrix(a, b):
    M =  [a[0], a[1], b[0], b[1]]
    Mx = [a[2], a[1], b[2], b[1]]
    My = [a[0], a[2], b[0], b[2]]
    return [M, Mx, My]
  
  
def main():
    print('Funcion para resolver ecuaciones de dos variables')
    print('Ingrese los valores de la ecuacion 1')
    ecuation1 = getData()
    print('Ingrese los valores de la ecuacion 2')
    ecuation2 = getData()
    resulte = result(determinant(matrix(ecuation1, ecuation2)))
    
    print("El resultado de las variables es:")
    print("x = " + str(resulte[0]))
    print("y = " + str(resulte[1]))
  
  
def getData():
    a = float(input("Ingrese el valor de 1: "))
    b = float(input("Ingrese el valor de 2: "))
    c = float(input("Ingrese el valor de 3: "))
    return [a, b, c]
  
  
if '__main__' == __name__:
    main()